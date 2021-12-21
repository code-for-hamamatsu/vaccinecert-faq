# コロナワクチン接種記録アプリFAQ

## ライセンス
本ソフトウェアは、[MITライセンス](./LICENSE.txt)の元提供されています。

# 開発者向け情報

## 1. 環境構築の手順

このFAQは 静的サイトジェネレータ [Hugo](https://gohugo.io/) を使用してサイトの構築を行います。

Dockerを使って開発する場合は`3.2. Dockerで起動する場合`から始めてください。

### 1.1. WindowsでScoopを使ってHugoをインストールする

> [Scoop](https://scoop.sh/)はWindowsのCLIでアプリケーションのインストールやバージョン管理などができるツールです。
Scoopの実行にはPowerShell 5（またはそれ以降、PowerShell Coreを含む）および.NET Framework 4.5（またはそれ以降）が必要です。
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
### 3.3. サイトの表示

ブラウザで http://localhost:1313 を開きます。
Live Reloadされるのでエディタで修正したものは即時反映されます。

## 4. ブランチルール

main 以外は、Pull Request は禁止です。
Pull Request を送る際のブランチは、以下のネーミングルールに従ったブランチにしてください。

| 種類 | ブランチのネーミングルール |
| ---- | ---- |
|機能追加系|`feature/{ISSUE_ID}-{branch_title_name}`|
|ホットフィックス系|`hotfix/{ISSUE_ID}-{branch_title_name}`|

### 4.1. 基本的なブランチ

| 目的 | ブランチ | 確認URL | Pull requestsを出せる人 | 備考 |
| ---- | ---- | ---- | ---- | ---- |
| 開発/本番 | main |  | 全開発者 | base branch。基本は、この`main`ブランチに Pull Requestを送ってください。 |

### 4.2. システムで利用しているブランチ

| 目的 | ブランチ | 確認URL | 備考 |
| ---- | -------- | ---- | ---- |
| 本番サイトHTML | main | https://vaccinecert-faq.code4japan.org/ | 静的ビルドされたHTMLが置いてある場所 |
| ステージングサイト HTML |  |  | 静的ビルドされたHTMLが置いてある場所 |

## 4.3. Issue へのコメントや Pull Request について
* Issue へのコメントはご自由にどうぞ！新しい質問や提案なども受け付けます。
* Issue を追加する場合、必ず既に同様の Issue が無いか検索をしてから作成してください。
* Pull Request を送る場合、必ず対応する Issue 番号を追記してください。単独の Pull Request は受け付けません。
* improve(改善提案)がついたIssueについては必ず反映できると限りませんのでご了承ください。

## 5. 本番サイトへのデプロイ
main ブランチがアップデートされると、Amplify Hostingにより本番サイトにデプロイされます。

## 6. 修正を行う場合の参考ドキュメント

本サイトの修正をするための参考資料は[カスタマイズ参考資料](./FOR_DEVELOPERS.md)にあるので参考にしてください。
