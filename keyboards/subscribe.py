from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import channel_link

subscribe_markup = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('📢Канал', channel_link)
    ],
    [
        InlineKeyboardButton('Я подписался✅', callback_data='i_am_subscribed')
    ]
])
