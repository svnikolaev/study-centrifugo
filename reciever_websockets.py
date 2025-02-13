import asyncio
import json
import os

import websockets
from dotenv import load_dotenv

load_dotenv()

CENTRIFUGO_WS_URL = os.getenv(
    'CENTRIFUGO_WS_URL', 'ws://localhost:8000/connection/websocket'
)
CHANNEL = os.getenv('CHANNEL', 'your-channel')
TOKEN = os.getenv('TOKEN')


async def connect(
    websocket: websockets.WebSocketServerProtocol, token: str
) -> None:
    """
    Подключается к серверу Centrifugo, используя токен.

    :param websocket: Веб-сокет, через который происходит общение
    :type websocket: websockets.WebSocketServerProtocol
    :param token: Токен, используемый для аутентификации
    :type token: str
    """
    print('Connecting to Centrifugo...')
    connect_command = json.dumps({
        "id": 1,
        "connect": {"token": token}
    })
    await websocket.send(connect_command)
    response = await websocket.recv()
    print('Connected to Centrifugo:', response)


async def subscribe(
    websocket: websockets.WebSocketServerProtocol, channel: str
) -> None:
    """
    Подписывается на канал на сервере Centrifugo, используя указанный
    веб-сокет. Отправляет команду subscribe, ожидает ответа и выводит
    информацию о результате подписки.

    :param websocket: Веб-сокет, через который происходит общение
    :type websocket: websockets.WebSocketServerProtocol
    :param channel: Канал, на который происходит подписка
    :type channel: str
    """
    print('Subscribing to channel...')
    subscribe_command = json.dumps({
        "id": 2,
        "subscribe": {"channel": channel}
    })
    await websocket.send(subscribe_command)
    response = await websocket.recv()
    print(f'Subscribed to channel: {channel}, response:', response)


async def receive_messages(
    websocket: websockets.WebSocketServerProtocol
) -> None:
    """
    Получает сообщения от сервера Centrifugo, используя указанный
    веб-сокет.

    Если получено PING-сообщение, отправляет PONG-ответ.
    """
    async for message in websocket:
        try:
            parsed_messages = json.loads(message)
            if isinstance(parsed_messages, list):
                print(f'RECEIVED MULTIPLE MESSAGES ({len(parsed_messages)}):')
                # Обработка нескольких JSON-объектов
                for msg in parsed_messages:
                    handle_message(msg)
            elif parsed_messages == {}:
                # Периодически Centrifugo отправляет PING сообщение
                # для поддержки WebSocket-соединения необходимо ответить
                # пустым сообщением
                print("🔧 Received PING...")
                await websocket.send(json.dumps({}))  # "{}" - тоже работает
                print("🔧 Sent PONG")
            else:
                handle_message(parsed_messages)
        except json.JSONDecodeError as e:
            print(f'Failed to decode message "{message}": {e}')


def handle_message(message: dict) -> None:
    """
    Обрабатывает полученное сообщение от сервера Centrifugo.

    Если сообщение содержит ошибку, выводит информацию об ошибке.
    Если сообщение является опубликованным событием, выводит о неминформацию.
    В общем случае выводит общую информацию о сообщении.

    :param message: Сообщение в виде словаря, полученное от сервера.
    :type message: dict
    """
    if 'error' in message:
        print(f'Received error: {message["error"]}')
    elif 'method' in message and message['method'] == 'published':
        print(f'Received published event: {message}')
    else:
        print(f'Received message: {message}')


async def main():
    async with websockets.connect(CENTRIFUGO_WS_URL) as websocket:
        # Соединение с Centrifugo и авторизация
        await connect(websocket, TOKEN)
        # Подписка на канал
        await subscribe(websocket, CHANNEL)
        # Запуск цикла обработки сообщений
        await receive_messages(websocket)


if __name__ == "__main__":
    asyncio.run(main())
