from aiogram.dispatcher.filters import BoundFilter
from keyboards import subscribe_markup
from loader import dp, channel_id


class IsChatMember(BoundFilter):

    async def check(self, update):
        user = update.from_user.id
        if (await dp.bot.get_chat_member(channel_id, user))['status'] != "left":
            return True

        await dp.bot.send_message(user, '❕ Для использования бота, подпишись на канал, бро:',
                                  reply_markup=subscribe_markup)
        return False
