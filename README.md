# コロナワクチン接種記録アプリFAQ

# 開発者向け情報

## 1. 環境構築の手順

このFAQは 静的サイトジェネレータ [Hugo](https://gohugo.io/) を使用してサイトの構築を行います。

Dockerを使って開発する場合は`3.2. Dockerで起動する場合`から始めてください。

### 1.1. WindowsでScoopを使ってHugoをインストールする

> [Scoop](https://scoop.sh/)はWindowsのCLIでアプリケーションのインストールやバージョン管理などができるツールです。
Scoopの実行にはPowerShell 5（またはそれ以降、PowerShell Coreを含む）および.NET Framework 4.5（またはそれ以降）が必要です
Scoopのインストールは https://scoop.sh/ を参考にして行ってください。

```powershell
# install hugo
$ scoop install hugo 
```

### 1.2. MacでHugoをインストールする

```bash
# install hugo
$ brew install hugo
```

### 1.3. UbuntuでHugoをインストールする

```bash
# install hugo
$ sudo apt install hugo
```

## 2. テーマのインストール

このサイトは Hugoのテーマ [Dot](https://themes.gohugo.io/themes/dot-hugo-documentation-theme/)を使用しています。

初回起動時は`themes`配下が空なので以下のコマンドを実行して読み込みを行います。

```
$ git submodule update --init
```

## 3. サイトの構築と表示

### 3.1. Windows,Mac,Ubuntu でバイナリでHugoをインストールした場合
``` bash
# serve with hot reload at localhost:1313
$ hugo server
```
### 3.2. Dockerで起動する場合

``` bash
$ docker-compose build
$ docker-compose up -d
$ docker exec -it vaccinecert-faq-hugo sh
```

## 4. ブランチルール

main 以外は、Pull Request は禁止です。
Pull Request を送る際のブランチは、以下のネーミングルールに従ったブランチにしてください。

| 種類 | ブランチのネーミングルール |
| ---- | ---- |
|機能追加系|`feature/#{ISSUE_ID}-#{branch_title_name}`|
|ホットフィックス系|`fix/#{ISSUE_ID}-#{branch_title_name}`|


## 5. GitHub Pagesへのデプロイ

main ブランチがアップデートされると、GitHub pagesへデプロイするGithub Action `.github/workflows/gh-pages.yml` があります

