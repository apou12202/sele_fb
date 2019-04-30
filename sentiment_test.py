import io
import json
import jieba
import re
from snownlp import SnowNLP
import pandas as pd

with io.open("output/text_splitted.json", 'r', encoding="utf-8") as file:
    text = json.load(file)

    data_len = len(text)
#
# for i in text:
#     s = SnowNLP(u"'" + i['review'] + "'")
#     print(s.sentiments)


sentiment_table = pd.read_excel('dict/sentiment_mod.xlsx')
sentiment_table.drop(['Unnamed: 10', 'Unnamed: 11'], inplace=True, axis=1)
pos_table = pd.read_excel('dict/sentiment_mod.xlsx', sheet_name='Sheet2')
neg_table = pd.read_excel('dict/sentiment_mod.xlsx', sheet_name='Sheet3')

pos_dict = dict(zip(list(pos_table.posword), list(pos_table.score)))
neg_dict = dict(zip(list(neg_table.negword), map(lambda a: a*(0-1), list(neg_table.score))))
sentiment_dict = {**pos_dict, **neg_dict}
#
# for w in sentiment_dict.keys():
#     jieba.suggest_freq(w, True)
#
# stop_words = [re.findall(r'\S+', w)[0] for w in open('dict/stopWords.txt', encoding='utf8').readlines() if len(re.findall(r'\S+', w)) > 0]
# def sent2word(sentence, stop_words = stop_words):
#     words = jieba.cut(sentence, HMM=False)
#     words = [w for w in words if w not in stop_words]
#     return words
#
#
# def get_sentment(sent):
#     tokens = sent2word(sent)
#     score = 0
#     countword = 0
#     for w in tokens:
#
#         if w in sentiment_dict.keys():
#             score += sentiment_dict[w]
#             countword += 1
#     if countword != 0:
#         return score / countword
#     else:
#         return 0
#
# sent ="我覺得海豚非常聰明"
# get_sentment(sent)
