from db import *
from loader import dp
from aiogram import types
from filters import IsAdmin, IsPrivate
from aiogram.dispatcher import FSMContext
from keyboards import admin_menu_markup, cancel_markup, admin_confirm_markup


@dp.message_handler(IsPrivate(), IsAdmin(), text='⛔Отмена',
                    state=['wait_code_delete', 'wait_code_add', 'wait_title_add', 'wait_about_add', 'wait_code_change',
                           'wait_title_change', 'wait_about_change'])
async def cancel_admin(message: types.Message, state: FSMContext):
    await state.reset_state()
    await message.answer('Отменено!', reply_markup=admin_menu_markup)


@dp.message_handler(IsPrivate(), IsAdmin(), text=['!admin', '/admin'], state="*")
async def admin_menu(message: types.Message, state: FSMContext):
    await state.reset_state()
    await message.answer('Админ-панель', reply_markup=admin_menu_markup)


@dp.message_handler(IsPrivate(), IsAdmin(), text='➕Добавить')
async def add_film(message: types.Message, state: FSMContext):
    await state.set_state('wait_code_add')
    await message.answer('Введите код', reply_markup=cancel_markup)


@dp.message_handler(IsPrivate(), IsAdmin(), content_types=['text'], state='wait_code_add')
async def add_film(message: types.Message, state: FSMContext):
    res = await check_code_exist(message.text)
    if res is not None:
        await message.answer('Такой код уже есть в базе! Введите что-то другое', reply_markup=cancel_markup)
        return
    await state.update_data(new_code=message.text)
    await state.set_state('wait_title_add')
    await message.answer('Введите титульник', reply_markup=cancel_markup)


@dp.message_handler(IsPrivate(), IsAdmin(), content_types=['text'], state='wait_title_add')
async def add_film(message: types.Message, state: FSMContext):
    await state.update_data(new_title=message.text)
    await state.set_state('wait_about_add')
    await message.answer('Введите описание', reply_markup=cancel_markup)


@dp.message_handler(IsPrivate(), IsAdmin(), content_types=['text'], state='wait_about_add')
async def add_film(message: types.Message, state: FSMContext):
    await state.update_data(new_about=message.text)
    await state.set_state('wait_confirm_add')
    data = await state.get_data()
    code = data['new_code']
    title = data['new_title']
    about = message.text
    text = f'''
<b>{title}</b>

{about}
    '''
    await message.answer(text, reply_markup=types.ReplyKeyboardRemove())
    await message.answer(f'Сохраняем под кодом {code}?', reply_markup=admin_confirm_markup)


@dp.callback_query_handler(IsPrivate(), IsAdmin(), state='wait_confirm_add', text='yes_admin')
async def confirmed_add_film(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    data = await state.get_data()
    code = data['new_code']
    title = data['new_title']
    about = data['new_about']
    await state.reset_state(with_data=True)

    res = await write_film(code, title, about)

    if not res:
        await call.message.answer('Возникла ошибка!', reply_markup=admin_menu_markup)
        return

    await call.message.answer('Успешно!', reply_markup=admin_menu_markup)


@dp.message_handler(IsPrivate(), IsAdmin(), text='⚙Изменить')
async def change_film(message: types.Message, state: FSMContext):
    await state.set_state('wait_code_change')
    await message.answer('Введите код фильма')


@dp.message_handler(IsPrivate(), IsAdmin(), content_types=['text'], state='wait_code_change')
async def change_film(message: types.Message, state: FSMContext):
    res = await check_code_exist(message.text)
    if res is None:
        await message.answer('Такого кода нет в базе! Введите что-то другое', reply_markup=cancel_markup)
        return
    await state.update_data(change_code=message.text)
    await state.set_state('wait_title_change')
    await message.answer('Введите титульник', reply_markup=cancel_markup)


@dp.message_handler(IsPrivate(), IsAdmin(), content_types=['text'], state='wait_title_change')
async def change_film(message: types.Message, state: FSMContext):
    await state.update_data(change_title=message.text)
    await state.set_state('wait_about_change')
    await message.answer('Введите описание', reply_markup=cancel_markup)


@dp.message_handler(IsPrivate(), IsAdmin(), content_types=['text'], state='wait_about_change')
async def change_film(message: types.Message, state: FSMContext):
    await state.update_data(change_about=message.text)
    await state.set_state('wait_confirm_change')
    data = await state.get_data()
    code = data['change_code']
    title = data['change_title']
    about = message.text
    text = f'''
<b>{title}</b>

{about}
    '''
    await message.answer(text, reply_markup=types.ReplyKeyboardRemove())
    await message.answer(f'Изменяем фильм с кодом {code}?', reply_markup=admin_confirm_markup)


@dp.callback_query_handler(IsPrivate(), IsAdmin(), state='wait_confirm_change', text='yes_admin')
async def confirmed_change_film(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    data = await state.get_data()
    code = data['change_code']
    title = data['change_title']
    about = data['change_about']
    await state.reset_state(with_data=True)

    res = await change_film_db(code, title, about)

    if not res:
        await call.message.answer('Возникла ошибка!', reply_markup=admin_menu_markup)
        return

    await call.message.answer('Успешно!', reply_markup=admin_menu_markup)


@dp.message_handler(IsPrivate(), IsAdmin(), text='➖Удалить')
async def delete_film(message: types.Message, state: FSMContext):
    await state.set_state('wait_code_delete')
    await message.answer('Введите код', reply_markup=cancel_markup)


@dp.message_handler(IsPrivate(), IsAdmin(), content_types=['text'], state='wait_code_delete')
async def delete_film(message: types.Message, state: FSMContext):
    res = await check_code_exist(message.text)
    if res is None:
        await message.answer('Такого кода нет в базе! Введите что-то другое', reply_markup=cancel_markup)
        return
    await state.update_data(delete_code=message.text)
    await state.set_state('wait_confirm_delete')
    await message.answer(f'Удаляем фильм под кодом {message.text}?', reply_markup=admin_confirm_markup)


@dp.callback_query_handler(IsPrivate(), IsAdmin(), state='wait_confirm_delete', text='yes_admin')
async def confirmed_change_film(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    data = await state.get_data()
    code = data['delete_code']
    await state.reset_state(with_data=True)

    res = await delete_film_db(code)

    if not res:
        await call.message.answer('Возникла ошибка!', reply_markup=admin_menu_markup)
        return

    await call.message.answer('Успешно!', reply_markup=admin_menu_markup)


@dp.callback_query_handler(IsPrivate(), IsAdmin(), state='wait_confirm_add', text='no_admin')
@dp.callback_query_handler(IsPrivate(), IsAdmin(), state='wait_confirm_change', text='no_admin')
@dp.callback_query_handler(IsPrivate(), IsAdmin(), state='wait_confirm_delete', text='no_admin')
async def non_confirmed_add_film(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await state.reset_state(with_data=True)
    await call.message.answer('Отменено!', reply_markup=admin_menu_markup)
