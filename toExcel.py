import json
import xlwings as xw
import sys
import io

workbook = xw.Book()

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8') # out utf-8

with open("output/CrossAnalyze/tsai/1.json", encoding='utf-8') as f:
    data = json.load(f)
    angry = data[0]['怒']
    angry_len = len(data[0]['怒'])

    love = data[1]['愛心']
    love_len = len(data[1]['愛心'])
    # print(len(data[0]['怒']))

    sheet = workbook.sheets['工作表1']
    sheet.cells(1, 1).value = '怒'

    for i in range(1, angry_len):
        sheet.cells(i + 1, 1).value = angry[i-1]

    sheet.cells(1, 2).value = '愛心'

    for i in range(1, love_len):
        sheet.cells(i + 1, 2).value = love[i-1]

workbook.save("output/CrossAnalyze/excel/tsai1.csv")
