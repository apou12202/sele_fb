import json
import love_get
import angry_get
import io
import time

url = "https://www.facebook.com/ufi/reaction/profile/browser/?ft_ent_identifier=ZmVlZGJhY2s6MjY0NDQ2MzQwODkwMzk5NQ%3D%3D&av=100001602414974"

angry = angry_get.main(url)

love = love_get.main(url)


task = [{
    "怒": angry
    },
    {
    "愛心": love
    }]

with io.open("output/CrossAnalyze/Lai3.json", 'w', encoding='utf-8') as file:
    json.dump(task, file, ensure_ascii=False, indent=4)















