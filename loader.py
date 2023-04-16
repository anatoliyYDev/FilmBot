from dotenv import load_dotenv
import os
from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging.config

load_dotenv()

from conf_log import logger_settings

logging.config.dictConfig(logger_settings)
logger = logging.getLogger('my_logger')

token = os.getenv('TOKEN')
channel_id = os.getenv('CHANNEL_ID')
channel_link = os.getenv('CHANNEL_LINK')
admins = os.getenv('ADMINS').split(',')

DB_PATH = "db/db.sqlite3"
DB_SQL_PATH = "db/db.sql"

bot = Bot(token, parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())