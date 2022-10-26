from aiogram import Dispatcher, Bot, types, md
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from random import randint
from dotenv import load_dotenv
import os

load_dotenv(".env")

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)

button1 = InlineKeyboardButton(text="👋 button1", callback_data="randomvalue_of10")
button2 = InlineKeyboardButton(text="💋 button2", callback_data="randomvalue_of100")
keyboard_inline = InlineKeyboardMarkup().add(button1, button2)

keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
    "👋 Hello!", "💋 Youtube"
)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer(f"Hello, {message.from_user.full_name}")


# ----
@dp.message_handler(commands=["random"])
async def random_answer(message: types.Message):
    await message.reply("Select a range:", reply_markup=keyboard_inline)


@dp.callback_query_handler(text=["randomvalue_of10", "randomvalue_of100"])
async def random_value(call: types.CallbackQuery):
    if call.data == "randomvalue_of10":
        await call.message.answer(randint(1, 10))
    if call.data == "randomvalue_of100":
        await call.message.answer(randint(1, 100))
    await call.answer()


# ----
@dp.message_handler()
async def check_language(message: types.Message):
    locale = message.from_user.locale

    await message.reply(
        md.text(
            md.bold("Info about your language:"),
            md.text("🔸", md.bold("Code:"), md.code(locale.language)),
            md.text("🔸", md.bold("Territory:"), md.code(locale.territory or "Unknown")),
            md.text("🔸", md.bold("Language name:"), md.code(locale.language_name)),
            md.text(
                "🔸", md.bold("English language name:"), md.code(locale.english_name)
            ),
            sep="\n",
        )
    )
