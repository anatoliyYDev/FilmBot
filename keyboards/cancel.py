from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

cancel_markup = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton('⛔Отмена')
    ]
], resize_keyboard=True)
