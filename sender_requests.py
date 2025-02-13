import os
import time
from datetime import datetime

import requests
from dotenv import load_dotenv

load_dotenv()

CENTRIFUGO_API_URL = os.getenv(
    'CENTRIFUGO_API_URL', 'http://localhost:8000/api'
)
CHANNEL = os.getenv('CHANNEL', 'your-channel')
API_KEY = os.getenv('API_KEY')


def send_message(message, api_key: str, url: str, channel: str) -> None:
    """
    Отправляет сообщение в канал на сервере Centrifugo, используя API.

    :param message: Сообщение, которое будет отправлено
    :type message: str
    :param api_key: Ключ API, используемый для аутентификации
    :type api_key: str
    :param url: URL, используемый для отправки запроса
    :type url: str
    :param channel: Канал, в который будет отправлено сообщение
    :type channel: str
    """
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'apikey {api_key}'
    }
    data = {
        'method': 'publish',
        'params': {
            'channel': channel,
            'data': message
        }
    }
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        print(f'Message sent successfully: {message}')
    else:
        print(f'Error sending message: {response.text}')


if __name__ == '__main__':
    while True:
        msg = {'content': datetime.isoformat(datetime.now())}
        send_message(
            msg,
            API_KEY,
            CENTRIFUGO_API_URL,
            CHANNEL
        )
        time.sleep(2)
