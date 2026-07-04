import os
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

TOKEN = os.getenv("8683974265:AAEDO5FnvCLIEMmgVeyT2aRv6jXoT-9DaTE")

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Укажи здесь свой Telegram ID
OWNER_ID = 8760172354


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "👋 Привет!\n\n"
        "Напиши сюда сообщение, и оно будет отправлено владельцу анонимно."
    )


@dp.message()
async def anonymous(message: Message):
    await bot.send_message(
        OWNER_ID,
        f"📩 Новое анонимное сообщение\n\n"
        f"👤 От: {message.from_user.full_name}\n"
        f"🆔 ID: {message.from_user.id}\n\n"
        f"💬 {message.text}"
    )

    await message.answer("✅ Сообщение отправлено анонимно!")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
