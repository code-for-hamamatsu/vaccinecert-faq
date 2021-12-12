# カスタマイズ参考資料
# 1. ディレクトリ構造

```
[ROOT]
├─.github
├─archetypes
├─content
│  ├─faq1
│  │   └─_index.ja.md
│  ├─faq2
│  ├─faq3
│  ├─faq4
│  ├─faq5
│  ├─faq6
│  └─faq7
├─data
│  └─faq
├─i18n
├─layouts
│  ├─partials
│  └─shortcodes
├─resources
│  └─_gen
│      ├─assets
│      └─images
├─static
│  └─images
└─themes
    └─dot-hugo
```

# 2. ディレクトリ構造説明 

各ディレクトリの概要を示します。

## content
すべてのFAQは、このディレクトリ内に存在します。カテゴリ別にフォルダを分けその中にFAQのコンテンツが置かれます。
カテゴリの追加があった場合はフォルダの追加を行いその中に他のフォルダからコンテンツファイル _index.ja.mdをコピーします。カテゴリの削除があった場合はフォルダごと削除します。
フォルダ名はカテゴリにアクセスするためのurlの名称になります。

faq2フォルダ内のカテゴリ
> https://code-for-hamamatsu.github.io/vaccinecert-faq/faq2/

## data
このディレクトリは、FAQの内容を書いたJSONファイルが置かれます。

## i18n
多言語化対応のためのキーワード設定ファイルの置き場所
## layouts
テーマをカスタマイズするためのファイルを置く場所
dotテーマの中に変更したいファイルがある場合は、同じ階層構造になるようにこのフォルダの中にコピーして、この中のファイルを修正してカスタマイズします。
> 直接themesフォルダの中のファイルを修正することは禁止します。

現在のFAQの表示では themes/_default/single.htmlが適用されています。
コンテンツフォルダと同じ名前のフォルダをlayoutsに作成することで個別にレイアウトを適用することができます。

## themes
元のテーマを置く場所
> 直接themesフォルダの中のファイルを修正することは禁止します。

# 3. FAQコンテンツファイルの書式

```
---
title: "ごみ・リサイクル"
draft: false
type : "docs"
weight : 1
---

{{< vaccinefaq category="ごみ・リサイクル" >}}
```

## コンテンツファイル記述説明

### title
カテゴリ名を指定します

### draft: false
ドラフト版か否か
ドラフト版の場合はページの生成は行われません

### type : "docs"
トップページのカテゴリボタンに表示する場合はこの値を`docs`にします

### weight
トップページに表示する場合の並び順になります。小さい順に左上から右下に整列します


## ショートコードによるFAQ表示

`data/faq/faq.json` に書かれたFAQを表示するためにショートコード (layouts/shortcodes/vaccinefaq.html)を使用して表示します 
`category=""`に指定した文字列でfaq.jsonの`カテゴリ1`に一致するデータを抽出します

```
{{< vaccinefaq category="ごみ・リサイクル" >}}
```
