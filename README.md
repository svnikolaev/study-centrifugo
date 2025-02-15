# Изучение Centrifugo

## Информация

[Клиентские SDK для работы с Centrifugo](https://centrifugal.dev/docs/transports/client_sdk)

1. [centrifuge-python](https://github.com/centrifugal/centrifuge-python):
    WebSocket real-time SDK for Centrifugo server
2. [pycent](https://github.com/centrifugal/pycent):
    Python SDK to communicate with Centrifugo v5 HTTP API

## Базовые команды

### Установить Centrifugo

[Документация по установке](https://centrifugal.dev/docs/getting-started/installation)

```sh
wget https://github.com/centrifugal/centrifugo/releases/download/v6.0.2/centrifugo_6.0.2_linux_amd64.tar.gz && tar -xzf centrifugo_6.0.2_linux_amd64.tar.gz
```

### Запустить Centrifugo

[Документация по началу работы](https://centrifugal.dev/docs/getting-started/quickstart)

```sh
./centrifugo genconfig
./centrifugo --config config.json
```

Чтобы разрешить всем авторизованным пользователям читать каналы, нужно добавить в `config.json`:

```json
  "channel": {
    "without_namespace": {
      "allow_subscribe_for_client": true
    }
  }
```

### Сформировать токен

- [Документация по началу работы](https://centrifugal.dev/docs/getting-started/quickstart)
- [Как сгенерировать JWT (token)](https://centrifugal.dev/docs/server/authentication)

Токен для подключения через websocket формируется на основе hmac_secret_key с помощью команды `./centrifugo gentoken`:

```sh
$ ./centrifugo gentoken -u 123333
HMAC SHA-256 JWT for user "123333" with expiration TTL 168h0m0s:
eyJhbGciOiJIUzI1NiIsCJ9.eyJzdWIiOiIxMjMzMzMiLzOfewqTQwNDAyNH0.DwkaLB0kxByKk4C_VuPCDT9KEGeJOHwU1N3H9-C6Lno
```
