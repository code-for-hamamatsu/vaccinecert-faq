# vaccinecert-faq

## setup

初回起動時は`themes`配下が空なので以下のコマンドを実行する。

```
$ git submodule update --init
```

### Dockerで起動する場合

```
$ docker-compose build
$ docker-compose up -d
$ docker exec -it vaccinecert-faq-hugo sh
```
