import os
import time
from datetime import datetime

from cent import Client, PublishRequest
from dotenv import load_dotenv

load_dotenv()

CENTRIFUGO_API_URL = os.getenv(
    'CENTRIFUGO_API_URL', 'http://localhost:8000/api'
)
CHANNEL = os.getenv('CHANNEL', 'your-channel')
API_KEY = os.getenv('API_KEY')


if __name__ == '__main__':
    client = Client(CENTRIFUGO_API_URL, API_KEY)
    while True:
        msg = {'content': datetime.isoformat(datetime.now())}
        request = PublishRequest(
            channel=CHANNEL,
            data=msg
        )
        result = client.publish(request)
        print(f'Message sent successfully: "{msg}", {result=}')
        time.sleep(2)
