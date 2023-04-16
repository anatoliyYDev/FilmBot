from loader import dp, logger
from aiogram import types
from filters import IsChatMember, IsPrivate, IsAdmin
from aiogram.dispatcher import FSMContext
from keyboards import cancel_markup, search_markup
from db import check_code_exist


@dp.message_handler(IsPrivate(), IsAdmin(), text="📛Выйти")
@dp.callback_query_handler(IsPrivate(), IsChatMember(), text='i_am_subscribed')
@dp.message_handler(IsPrivate(), IsChatMember(), content_types=['text'])
async def start_message(update: types.Message | types.CallbackQuery, state: FSMContext):
    await state.set_state('wait_code')
    match update:
        case types.Message():
            await update.answer('Введите код фильма', reply_markup=cancel_markup)
        case types.CallbackQuery():
            await update.message.delete()
            await update.message.answer('Введите код фильма', reply_markup=cancel_markup)


@dp.message_handler(IsPrivate(), IsChatMember(), state='wait_code', text="⛔Отмена")
async def cancel(message: types.Message, state: FSMContext):
    await state.reset_state()
    await message.answer('Отменено!', reply_markup=search_markup)


@dp.message_handler(IsPrivate(), IsChatMember(), state='wait_code')
async def search(message: types.Message, state: FSMContext):
    await state.reset_state()
    res = await check_code_exist(message.text)

    if res is None:
        await message.answer('Не найдено!', reply_markup=search_markup)
        return

    title = res[1]
    about = res[2]

    text = f'''
<b>{title}</b>

{about}
    '''

    await message.answer(text, reply_markup=search_markup)
    logger.info(f"Пользователь {message.from_user.id}(@{message.from_user.username}) нашел фильм {title} по коду {message.text}")


