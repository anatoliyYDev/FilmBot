from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

admin_menu_markup = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton('➕Добавить'),
        KeyboardButton('➖Удалить')
    ],
    [
        KeyboardButton('⚙Изменить')
    ],
    [
        KeyboardButton("📛Выйти")
    ]
], resize_keyboard=True)


admin_confirm_markup = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Да', callback_data='yes_admin'),
        InlineKeyboardButton('Нет', callback_data='no_admin')
    ]
])


