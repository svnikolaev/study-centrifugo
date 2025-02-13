# Изучение Centrifugo

## Установить Centrifugo

[Документация по установке](https://centrifugal.dev/docs/getting-started/installation)

```sh
wget https://github.com/centrifugal/centrifugo/releases/download/v6.0.2/centrifugo_6.0.2_linux_amd64.tar.gz && tar -xzf centrifugo_6.0.2_linux_amd64.tar.gz
```

## Запустить Centrifugo

[Документация по началу работы](https://centrifugal.dev/docs/getting-started/quickstart)

```sh
./centrifugo genconfig
./centrifugo --config config.json
```

## Сформировать токен

[Документация по началу работы](https://centrifugal.dev/docs/getting-started/quickstart)

Токен для подключения через websocket формируется на основе hmac_secret_key с помощью команды `./centrifugo gentoken`:

```sh
$ ./centrifugo gentoken -u 123333
HMAC SHA-256 JWT for user "123333" with expiration TTL 168h0m0s:
eyJhbGciOiJIUzI1NiIsCJ9.eyJzdWIiOiIxMjMzMzMiLzOfewqTQwNDAyNH0.DwkaLB0kxByKk4C_VuPCDT9KEGeJOHwU1N3H9-C6Lno
```
