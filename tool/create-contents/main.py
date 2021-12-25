# coding:utf-8
import json
import string
import hashlib
import os
import glob
import datetime

with open('./data/faq/faq.json', 'rb') as fin:
    faqs = json.load(fin)  # ファイルオブジェクトをオブジェクトに変換


template = '''
---
title: ${question}
question_no: ${question_no}
draft: false
weight: ${weight}
categories: ${category}
lastmod: ${lastmod}
---

{{< vaccinefaq>}}
${answer}
{{</ vaccinefaq>}}
'''


def create_contents(content, template):
    category = content['カテゴリ名']
    [category_no, category_name] = category.split('_', 2)
    category = "{:02d}".format(int(category_no)) + '_' + category_name

    question_no = f"Q{category_no}-{content['カテゴリ内No']}"
    question = f"{question_no} {content['質問']}"
    answer = content['回答']
    lastmod = datetime.datetime.strptime(
        content['更新日'], '%Y%m%d').strftime('%Y-%m-%d')
    weight = int(category_no)*100 + int(content['カテゴリ内No'])

    template_text = string.Template(template)
    result = template_text.safe_substitute(
        {'weight': weight, 'question_no': question_no, 'category': category, 'question': question, 'answer': answer, 'lastmod': lastmod})
    return result


contents = glob.glob('./content/faq/*.md')

for content_file in contents:
    try:
        os.remove(content_file)
    except OSError as e:
        print(f"Error:{ e.strerror}")

for faq in faqs:
    category = faq['カテゴリ名']
    [category_no, category_name] = category.split('_', 2)
    sub_no = faq['カテゴリ内No']
    question_no = f"Q{category_no}-{sub_no}"
    no = faq['No']

    title = faq['質問']
    file_hash = hashlib.md5(title.encode()).hexdigest()
    dirpath = './content/faq'
    filename = no + '.ja.md'
    filepath = os.path.join(dirpath, filename)
    with open(filepath, mode='w', encoding='UTF-8') as f:
        f.write(create_contents(faq, template))
