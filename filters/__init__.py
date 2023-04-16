from run import dp
from .admin import IsAdmin
from .chat_member import IsChatMember
from .private_chat import IsPrivate

if __name__ == "filters":
    dp.filters_factory.bind(IsAdmin)
    dp.filters_factory.bind(IsChatMember)
    dp.filters_factory.bind(IsPrivate)
