import sys
import os
import json

import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
_consoleHandler = logging.StreamHandler(sys.stdout)
_consoleHandler.setLevel(logging.INFO)
_simpleFormatter = logging.Formatter(
    fmt='%(levelname)-5s %(funcName)-20s %(lineno)4s: %(message)s'
)
_consoleHandler.setFormatter(_simpleFormatter)
logger.addHandler(_consoleHandler)

def main():
    try:
        json_file = sys.argv[1]
        content_dir_path = sys.argv[2]

        json_data = json.load(open(json_file, 'r'))
        category_template = read_category_template()
        faq_template = read_faq_template()

        dict_contents = {}
        for item in json_data:
            create_faq_md(content_dir_path, faq_template, item)
            if not item['カテゴリNo'] in dict_contents:
                dict_contents[item['カテゴリNo']] = item['カテゴリ名']
                create_category_md(content_dir_path, category_template, item)

    except Exception as e:
        logger.exception(e)
        raise e

def create_category_md(content_dir_path, category_template, item):
    target_category_md_path = os.path.join(content_dir_path, category_md_file_name(item))
    text = category_template
    text = text.replace('{{category}}', item['カテゴリ名'])
    text = text.replace('{{category-no}}', item['カテゴリNo'])
    text = text.replace('{{category-no-num}}', str(int(item['カテゴリNo'])))
    write_file(target_category_md_path, text)

def create_faq_md(content_dir_path, faq_template, item):
    target_faq_md_path = os.path.join(content_dir_path, faq_md_file_name(item))
    text = faq_template
    text = text.replace('{{question}}', item['質問'])
    text = text.replace('{{no}}', item['No'])
    text = text.replace('{{category-no}}', item['カテゴリNo'])
    text = text.replace('{{category-sub-no}}', item['カテゴリ内No'])
    write_file(target_faq_md_path, text)

def write_file(path, text):
    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))
    
    with open(path, 'w+') as f:
        f.write(text)
    
def faq_md_file_name(item):
    return 'faq/{0}/{1}-{2}.ja.md'.format(item['カテゴリNo'], item['カテゴリ内No'], item['No'])

def category_md_file_name(item):
    return 'categories/{0}.ja.md'.format(item['カテゴリNo'])

def read_faq_template():
    return read_template('template/faq.md')

def read_category_template():
    return read_template('template/category.md')

def read_template(filename):
    with open(os.path.join(os.path.dirname(__file__), filename), 'r') as f:
        return f.read()

if __name__ == '__main__':
    main()