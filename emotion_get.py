import json
import love_get
import angry_get
import io
import os

url = input("URL:")
data_dir = input("DATA DIR ADDRESS:")
data_name = input("DATA NAME:")

angry = angry_get.main(url)

love = love_get.main(url)


task = [{
    "怒": angry
    },
    {
    "愛心": love
    }]

if not os.path.exists("output/CrossAnalyze/" + data_dir):
    os.mkdir("output/CrossAnalyze/" + data_dir)

with io.open("output/CrossAnalyze/" + data_dir + "/" + data_name + ".json", 'w', encoding='utf-8') as file:
    json.dump(task, file, ensure_ascii=False, indent=4)

print("Done")













