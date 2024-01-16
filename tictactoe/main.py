TOKEN = "6938317584:AAEDuV_GArP4hd_hg0WINUofffeDHQLTuvY"

import asyncio
import logging

from handlers import game_handler

from aiogram import Bot, Dispatcher


# Запуск процесса поллинга новых апдейтов
async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.include_router(game_handler.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())