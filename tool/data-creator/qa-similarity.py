import numpy
import MeCab
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import json
import logging
import sys

# Logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# 形態素解析 Tokenizer
def tokenizer(text):
    t = MeCab.Tagger()
    return t.parse(text).split()

# 文書ベクトル化
def vector_array(documents):
    docs = numpy.array(documents)
    # 単語の出現回数を考慮せずにベクトル化
    vectorizer = TfidfVectorizer(analyzer=tokenizer, binary=True, use_idf=False)
    vecs = vectorizer.fit_transform(docs)
    return vecs.toarray()

# JSON ファイルからデータを読み込み
def data_load(file_name):
    with open(file_name, 'r') as file:
        return json.load(file)

# データから質問と回答を評価用の文章として抽出
def qa_extract(data):
    docs = []
    for faq in data:
        docs.append(faq['質問'] + faq['回答'])
    return docs

# 各文書の類似度上位 n 個を抽出
def sims_extract(data, cos_array, topn):
    sims_array = []
    i = 0
    for faq in data:
        cos = cos_array[i]
        # 自文書を含む上位 n+1 個の index を抽出（未ソート）
        topn_indices = numpy.argpartition(-cos, (topn + 1))[:(topn + 1)]
        # 上位 n+1 個の index を類似度で降順ソート
        tmp_indices = cos[topn_indices]
        indices = numpy.argsort(-tmp_indices)
        topn_indices_sorted = topn_indices[indices]
        # 自文書以外を抽出
        sim_array = []
        for idx in topn_indices_sorted:
            if idx != i:
                sim_item = {
                    'No': data[idx]['No'],
                    '質問': data[idx]['質問']
                }
                sim_array.append(sim_item)
        item = {
            'No': faq['No'],
            '類似質問': sim_array
        }
        sims_array.append(item)
        i += 1
    return sims_array

def main():
    try:
        json_file = sys.argv[1]
        topn = int(sys.argv[2])
        # データ読み込み
        data = data_load(json_file)
        # 評価用の文書を抽出・配列化
        qa_array = qa_extract(data)
        # 類似度計算
        cos_array = cosine_similarity(vector_array(qa_array), vector_array(qa_array))
        # 上位 n 個を抽出
        result = sims_extract(data, cos_array, topn)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except Exception as e:
        logger.exception(e)
        raise e

if __name__ == '__main__':
    main()