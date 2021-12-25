import sys
sys.dont_write_bytecode = True
import os
import json
from retry import retry
import requests
import pandas as pd
import io
import re

import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

CSV_ADDRESS = 'https://cio.go.jp/sites/default/files/uploads/documents/VaccinecertFAQ.csv'

@retry(tries=3, delay=1)
def get_csv_data(csv_address):
    res = requests.get(csv_address).content
    data = pd.read_csv(io.StringIO(res.decode("utf-8")), header=None, sep=",", engine="python")
    return data
    
def convert_to_json_data(data_csv):
    list_no = data_csv.iloc[:, 0]
    list_category = data_csv.iloc[:, 1]
    list_subno = data_csv.iloc[:, 2]
    list_q = data_csv.iloc[:, 3]
    list_a = data_csv.iloc[:, 4]
    list_updated = data_csv.iloc[:, 5]

    results_json = []
    for n in range(len(data_csv)):
        keyvalue = {}
        keyvalue = {
            'No': str(list_no[n]), 
            'カテゴリ名': list_category[n], 
            'カテゴリ内No': str(list_subno[n]), 
            '質問': list_q[n], 
            '回答': convert_answer(list_a[n]), 
            '更新日': str(list_updated[n])
        }
        results_json.append(keyvalue)
        
    return results_json

def convert_answer(text):
    text = replace_parentheses_enclosing_url_to_halfwidth(text)
    return text

# URLを囲む全角カッコを半角にする
# (マークダウンでリンクと認識させるため)
def replace_parentheses_enclosing_url_to_halfwidth(text):
    ary = re.findall('https?://[\w/:%#\$&\?\(\)~\.=\+\-]+', text)
    if ary == None or len(ary) == 0 or text.find('（') < 0:
        return text

    for item in ary:
        before = '（' + item + '）'
        after  = ' (' + item + ') '  # 見栄えのために前後に半角スペースを付与
        text   = text.replace(before, after)

    return text

def main():
    try:
        data_csv = get_csv_data(CSV_ADDRESS)
        data_json = convert_to_json_data(data_csv)
        print(json.dumps(data_json, ensure_ascii=False, indent=2))
    except Exception as e:
        logger.exception(e)
        raise e

if __name__ == '__main__':
    main()