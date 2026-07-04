import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

TOKEN = "8683974265:AAEDO5FnvCLIEMmgVeyT2aRv6jXoT-9DaTE"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "👋 Привет!\n\n"
        "Напиши сюда сообщение, и оно будет отправлено владельцу бота анонимно."
    )

@dp.message()
async def anonymous(message: Message):
    owner_id = 123456789  # Потом заменим на твой Telegram ID

    await bot.send_message(
        owner_id,
        f"📩 Новое анонимное сообщение:\n\n{message.text}"
    )

    await message.answer("✅ Сообщение отправлено анонимно!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
