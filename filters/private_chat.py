from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message, CallbackQuery


class IsPrivate(BoundFilter):

    async def check(self, update):
        user = update.from_user.id
        chat_type = None
        if type(update) == CallbackQuery:
            chat_type = update.message.chat.type
        elif type(update) == Message:
            chat_type = update.chat.type

        if chat_type != 'private':
            return False

        return True
