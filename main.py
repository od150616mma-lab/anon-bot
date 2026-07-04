import os
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Твой Telegram ID
OWNER_ID = 8760172354


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "👋 Привет!\n\n"
        "Напиши сюда сообщение, и оно будет отправлено владельцу анонимно."
    )


@dp.message(Command("r"))
async def reply_command(message: Message):
    if message.from_user.id != OWNER_ID:
        return

    parts = message.text.split(maxsplit=2)

    if len(parts) < 3:
        await message.answer(
            "Использование:\n"
            "/r ID сообщение"
        )
        return

    try:
        user_id = int(parts[1])
    except ValueError:
        await message.answer("❌ ID должен быть числом.")
        return

    text = parts[2]

    try:
        await bot.send_message(
            chat_id=user_id,
            text=f"💬 Анонимный ответ:\n\n{text}"
        )
        await message.answer("✅ Ответ отправлен!")
    except Exception as e:
        await message.answer(f"❌ Ошибка: {e}")


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
