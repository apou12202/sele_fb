import xlsxwriter
import json
from collections import Counter

# book = xlsxwriter.Workbook('output/CrossAnalyze/excel/han.xlsx')
#
# sheet1 = book.add_worksheet("angry")
# sheet1.write(0, 0, "name")
# sheet1.write(0, 1, "times")
#
# sheet2 = book.add_worksheet("love")
# sheet2.write(0, 0, "name")
# sheet2.write(0, 1, "times")
#
# d1 = json.load(open("output\CrossAnalyze\han\\1.json", encoding='utf-8'))
# d2 = json.load(open("output\CrossAnalyze\han\\2.json", encoding='utf-8'))
# d3 = json.load(open("output\CrossAnalyze\han\\3.json", encoding='utf-8'))
# d4 = json.load(open("output\CrossAnalyze\han\\4.json", encoding='utf-8'))
# d5 = json.load(open("output\CrossAnalyze\han\\5.json", encoding='utf-8'))
#
# angry_list = d1[0]['怒']
# angry_list += d2[0]['怒']
# angry_list += d3[0]['怒']
# angry_list += d4[0]['怒']
# angry_list += d5[0]['怒']
# # print(d1[0]['怒'])
#
# love_list = d1[1]['愛心']
# love_list += d2[1]['愛心']
# love_list += d3[1]['愛心']
# love_list += d4[1]['愛心']
# love_list += d5[1]['愛心']
#
# c = Counter(angry_list)
#
# i = 1
# for (k, v) in c.items():
#     if i < int(len(c.keys())):
#         sheet1.write(i, 0, k)
#         sheet1.write(i, 1, v)
#     i += 1
#
# c = Counter(love_list)
#
# j = 1
# for (k, v) in c.items():
#     if j < int(len(c.keys())):
#         sheet2.write(j, 0, k)
#         sheet2.write(j, 1, v)
#     j += 1
#
# book.close()

# ----------------------------------------HAN-------------------------------------------------------

# book = xlsxwriter.Workbook('output/CrossAnalyze/excel/kuo.xlsx')
#
# sheet1 = book.add_worksheet("angry")
# sheet1.write(0, 0, "name")
# sheet1.write(0, 1, "times")
#
# sheet2 = book.add_worksheet("love")
# sheet2.write(0, 0, "name")
# sheet2.write(0, 1, "times")
#
# d1 = json.load(open("output\CrossAnalyze\kuo\\1.json", encoding='utf-8'))
# d2 = json.load(open("output\CrossAnalyze\kuo\\2.json", encoding='utf-8'))
# d3 = json.load(open("output\CrossAnalyze\kuo\\3.json", encoding='utf-8'))
# d4 = json.load(open("output\CrossAnalyze\kuo\\4.json", encoding='utf-8'))
#
# angry_list = d1[0]['怒']
# angry_list += d2[0]['怒']
# angry_list += d3[0]['怒']
# angry_list += d4[0]['怒']
# # print(d1[0]['怒'])
#
# love_list = d1[1]['愛心']
# love_list += d2[1]['愛心']
# love_list += d3[1]['愛心']
# love_list += d4[1]['愛心']
#
# c = Counter(angry_list)
#
# i = 1
# for (k, v) in c.items():
#     if i < int(len(c.keys())):
#         sheet1.write(i, 0, k)
#         sheet1.write(i, 1, v)
#     i += 1
#
# c = Counter(love_list)
#
# j = 1
# for (k, v) in c.items():
#     if j < int(len(c.keys())):
#         sheet2.write(j, 0, k)
#         sheet2.write(j, 1, v)
#     j += 1
#
# book.close()

# -----------------------------------------KUO----------------------------------------------------------------------

# book = xlsxwriter.Workbook('output/CrossAnalyze/excel/lai.xlsx')
#
# sheet1 = book.add_worksheet("angry")
# sheet1.write(0, 0, "name")
# sheet1.write(0, 1, "times")
#
# sheet2 = book.add_worksheet("love")
# sheet2.write(0, 0, "name")
# sheet2.write(0, 1, "times")
#
# d1 = json.load(open("output\CrossAnalyze\lai\\1.json", encoding='utf-8'))
# d2 = json.load(open("output\CrossAnalyze\lai\\2.json", encoding='utf-8'))
# d3 = json.load(open("output\CrossAnalyze\lai\\3.json", encoding='utf-8'))
# d4 = json.load(open("output\CrossAnalyze\lai\\4.json", encoding='utf-8'))
# d5 = json.load(open("output\CrossAnalyze\lai\\5.json", encoding='utf-8'))
# d6 = json.load(open("output\CrossAnalyze\lai\\6.json", encoding='utf-8'))
# d7 = json.load(open("output\CrossAnalyze\lai\\7.json", encoding='utf-8'))
#
#
# angry_list = d1[0]['怒']
# angry_list += d2[0]['怒']
# angry_list += d3[0]['怒']
# angry_list += d4[0]['怒']
# angry_list += d5[0]['怒']
# angry_list += d6[0]['怒']
# angry_list += d7[0]['怒']
# # print(d1[0]['怒'])
#
# love_list = d1[1]['愛心']
# love_list += d2[1]['愛心']
# love_list += d3[1]['愛心']
# love_list += d4[1]['愛心']
# love_list += d5[1]['愛心']
# love_list += d6[1]['愛心']
# love_list += d7[1]['愛心']
# c = Counter(angry_list)
# i = 1
#
# for (k, v) in c.items():
#     if i < int(len(c.keys())):
#         sheet1.write(i, 0, k)
#         sheet1.write(i, 1, v)
#     i += 1
#
# c = Counter(love_list)
# j = 1
#
# for (k, v) in c.items():
#     if j < int(len(c.keys())):
#         sheet2.write(j, 0, k)
#         sheet2.write(j, 1, v)
#     j += 1
#
# book.close()

# ---------------------------------LAI--------------------------------------------------------------------------

book = xlsxwriter.Workbook('output/CrossAnalyze/excel/tsai.xlsx')

sheet1 = book.add_worksheet("angry")
sheet1.write(0, 0, "name")
sheet1.write(0, 1, "times")

sheet2 = book.add_worksheet("love")
sheet2.write(0, 0, "name")
sheet2.write(0, 1, "times")

d1 = json.load(open("output\CrossAnalyze\\tsai\\1.json", encoding='utf-8'))
d2 = json.load(open("output\CrossAnalyze\\tsai\\2.json", encoding='utf-8'))
d3 = json.load(open("output\CrossAnalyze\\tsai\\3.json", encoding='utf-8'))
d4 = json.load(open("output\CrossAnalyze\\tsai\\4.json", encoding='utf-8'))
d5 = json.load(open("output\CrossAnalyze\\tsai\\5.json", encoding='utf-8'))
d6 = json.load(open("output\CrossAnalyze\\tsai\\6.json", encoding='utf-8'))
d7 = json.load(open("output\CrossAnalyze\\tsai\\7.json", encoding='utf-8'))
d8 = json.load(open("output\CrossAnalyze\\tsai\\8.json", encoding='utf-8'))
d9 = json.load(open("output\CrossAnalyze\\tsai\\9.json", encoding='utf-8'))
d10 = json.load(open("output\CrossAnalyze\\tsai\\10.json", encoding='utf-8'))

angry_list = d1[0]['怒']
angry_list += d2[0]['怒']
angry_list += d3[0]['怒']
angry_list += d4[0]['怒']
angry_list += d5[0]['怒']
angry_list += d6[0]['怒']
angry_list += d7[0]['怒']
angry_list += d8[0]['怒']
angry_list += d9[0]['怒']
angry_list += d10[0]['怒']
# print(d1[0]['怒'])

love_list = d1[1]['愛心']
love_list += d2[1]['愛心']
love_list += d3[1]['愛心']
love_list += d4[1]['愛心']
love_list += d5[1]['愛心']
love_list += d6[1]['愛心']
love_list += d7[1]['愛心']
love_list += d8[1]['愛心']
love_list += d9[1]['愛心']
love_list += d10[1]['愛心']
c = Counter(angry_list)

i = 1
for (k, v) in c.items():
    if i < int(len(c.keys())):
        sheet1.write(i, 0, k)
        sheet1.write(i, 1, v)
    i += 1

c = Counter(love_list)

j = 1
for (k, v) in c.items():
    if j < int(len(c.keys())):
        sheet2.write(j, 0, k)
        sheet2.write(j, 1, v)
    j += 1

book.close()