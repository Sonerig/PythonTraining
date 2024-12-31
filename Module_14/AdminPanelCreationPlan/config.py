from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

API = None
bot = Bot(token=None)
dp = Dispatcher(bot, storage=MemoryStorage())
