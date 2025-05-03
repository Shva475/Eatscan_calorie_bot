import logging
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import requests

# Загрузить переменные из .env
load_dotenv()

# Получить ключ из переменной окружения (если решишь подключить OpenAI)
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

TOKEN = '7529633398:AAHqlu24h-OYP-kLO2BUHPtFd7xz7fDtxiU'

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Отправь мне фото еды, и я скажу, сколько в ней калорий!')

def analyze_image(photo_url):
    # Здесь можно добавить логику анализа фото с помощью API (например, OpenAI или другой сервис).
    # Для примера, вернём фиктивный результат.
    return "500 калорий"  # Пример возвращаемого значения (можно заменить на логику с реальным API)

def photo(update: Update, context: CallbackContext) -> None:
    photo_file = update.message.photo[-1].get_file()
    photo_url = photo_file.file_path
    update.message.reply_text(f'Фото получено! Сейчас анализирую калории...')

    # Получаем анализ калорий
    result = analyze_image(photo_url)

    # Отправляем результат пользователю
    update.message.reply_text(f'Примерное количество калорий: {result}')

def error(update: Update, context: CallbackContext) -> None:
    logger.warning('Ошибка "%s" при обновлении "%s"', context.error, update)

def main():
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.photo, photo))
    dispatcher.add_error_handler(error)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
