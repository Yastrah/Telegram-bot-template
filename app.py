import asyncio
import logging
import os
from dotenv import load_dotenv, find_dotenv

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from bot.routers import include_all_routers
from bot.config_reader import config

from bot.services.database import init_models

VERSION = "1.0.3"
load_dotenv(find_dotenv())

logger = logging.getLogger(__name__)


async def main():
    logging.getLogger("aiogram").setLevel("WARNING")
    logging.getLogger("aiosqlite").setLevel("WARNING")
    logging.getLogger("asyncio").setLevel("INFO")

    # logging.basicConfig(filename=f"logs/{datetime.datetime.now().strftime('%Y_%m_%d')}.log",
    #                     format="%(asctime)s [%(levelname)s] %(name)s: %(message)s", level="DEBUG",
    #                     datefmt="%Y-%m-%d %H:%M:%S", filemode='a')
    logging.basicConfig(
        format=config.logging.format,
        datefmt=config.logging.datefmt,
        level="DEBUG" if config.logging.debug else "INFO",
    )

    await init_models()

    bot = Bot(token=os.getenv('BOT_TOKEN'), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await bot.delete_webhook(drop_pending_updates=True)  # skip updates while was offline

    dp = Dispatcher()
    include_all_routers(dp)  # including routers
    logger.info(f"App version: {VERSION}\nStart polling...")
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.warning("Bot stopped!")
