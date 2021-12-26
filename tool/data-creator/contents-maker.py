import sys
import os
import json
import shutil

import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def main():
    try:
        # コマンドライン引数の取得
        # - faq.jsonファイル相対パス
        # - contentフォルダ相対パス
        json_file = sys.argv[1]
        content_dir_path = sys.argv[2]
        
        # 入力ファイル(faq.json と テンプレート)読み込み
        json_data = json.load(open(json_file, 'r'))
        category_template = read_category_template()
        faq_template = read_faq_template()

        # 事前に対象コンテンツフォルダ(categories, faq)を全削除しておく
        remove_target_contents(content_dir_path)

        # faq.jsonの内容をもとに、category用mdやqa用mdを生成する
        dict_contents = {}
        for item in json_data:
            create_faq_md(content_dir_path, faq_template, item)
            if not item['カテゴリNo'] in dict_contents:
                dict_contents[item['カテゴリNo']] = item['カテゴリ名']
                create_category_md(content_dir_path, category_template, item)

    except Exception as e:
        logger.exception(e)
        raise e

# カテゴリ用mdの生成
def create_category_md(content_dir_path, category_template, item):
    target_category_md_path = os.path.join(content_dir_path, category_md_file_name(item))
    text = category_template
    text = text.replace('{{category}}', item['カテゴリ名'])
    text = text.replace('{{category-no}}', item['カテゴリNo'])
    text = text.replace('{{category-no-num}}', str(int(item['カテゴリNo'])))
    write_file(target_category_md_path, text)

# FAQ用mdの生成
def create_faq_md(content_dir_path, faq_template, item):
    target_faq_md_path = os.path.join(content_dir_path, faq_md_file_name(item))
    text = faq_template
    text = text.replace('{{question}}', item['質問'])
    text = text.replace('{{no}}', item['No'])
    text = text.replace('{{category-no}}', item['カテゴリNo'])
    text = text.replace('{{category-sub-no}}', item['カテゴリ内No'])
    write_file(target_faq_md_path, text)

# ファイル生成
def write_file(path, text):
    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))
    
    with open(path, 'w+') as f:
        f.write(text)

# faq用mdファイル名取得
def faq_md_file_name(item):
    return 'faq/{0}/{1}-{2}.ja.md'.format(item['カテゴリNo'], item['カテゴリ内No'], item['No'])

# category用mdファイル名取得
def category_md_file_name(item):
    return 'categories/{0}.ja.md'.format(item['カテゴリNo'])
    
# 生成対象のコンテンツを削除する
# - content/categories/*
# - content/faq/*
def remove_target_contents(content_dir_path):
    remove_dir_all(os.path.join(content_dir_path, 'categories/'))
    remove_dir_all(os.path.join(content_dir_path, 'faq/'))
    
# フォルダ内全削除
def remove_dir_all(path):
    if os.path.exists(path):
        shutil.rmtree(path)

# faqテンプレートの読み込み
def read_faq_template():
    return read_template('template/faq.md')

# categoryテンプレートの読み込み
def read_category_template():
    return read_template('template/category.md')

# テンプレートの読み込み
def read_template(filename):
    with open(os.path.join(os.path.dirname(__file__), filename), 'r') as f:
        return f.read()

if __name__ == '__main__':
    main()