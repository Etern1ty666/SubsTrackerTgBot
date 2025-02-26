import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import FSInputFile
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
import os
from dotenv import load_dotenv
load_dotenv()

logging.basicConfig(level=logging.INFO)
bot = Bot(token=str(os.getenv('TG_BOT_TOKEN')))
dp = Dispatcher()
image_file = FSInputFile("SubsTrackerBotWelcomePicture.jpg")


@dp.message()
async def cmd_start(message: types.Message):
    keyboard = InlineKeyboardMarkup(row_width=1, inline_keyboard=[
                                          [
                                              InlineKeyboardButton(text='Запустить SubsTracker',
                                                                   web_app=WebAppInfo(url=f'https://substracker.ru/'))
                                          ]
                                      ])

    await message.answer_photo(photo=image_file, reply_markup=keyboard,
                               caption="🌟 Добро пожаловать в SubsTracker! 🎉\n\n"
                                       "SubsTracker помогает отслеживать ваши подписки и периодические платежи.\n\n"
                                       "Что можно делать вместе с SubsTracker:\n"
                                       "🔔 Вы активировали пробный период, и не хотите дальше пользоваться сервисом - "
                                       "напомним перед окончанием пробного периода.\n"
                                       "💰 Узнать свои траты, расходы за период и посмотреть статистику по категориям.\n"
                                       "📆 Возможность планировать траты и не забывать о предстоящих платежах.\n\n"
                                       "Приложение бесплатное! 🌟\n\n"
                                       "Давайте начнем! 🚀"
                               )


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
