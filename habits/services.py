import datetime

import requests
from config.settings import TELEGRAM_URL, TELEGRAM_TOKEN


def send_telegram_message(chat_id, message):
    """
    Отправляет сообщение в телеграм чат
    """
    params = {
        'chat_id': chat_id,
        'text': message
    }
    requests.get(f'{TELEGRAM_URL}{TELEGRAM_TOKEN}/sendMessage', params=params)
