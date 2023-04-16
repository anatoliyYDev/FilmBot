from aiogram.dispatcher.filters import BoundFilter
from aiogram import types
from loader import admins


class IsAdmin(BoundFilter):

    async def check(self, message: types.Message):
        user = message.from_user.id
        if str(user) in admins:
            return True

        return False

