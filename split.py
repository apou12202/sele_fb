import json
import io


#  處理留言
def split():
    text_splitted = []

    with io.open("output/text_split.json", 'r', encoding='utf-8') as file:
        test = json.load(file)
        data_len = len(test)

    for i in range(data_len):
        text = {
            "reviewer": test[i]['reviewer'],
            "review": test[i]['review'].replace(test[i]['reviewer'] + ' ', '')  # 用空字串取代留言區名字+空格
        }
        text_splitted.append(text)

    with io.open("output/text_splitted.json", 'w', encoding='utf-8') as file:
        json.dump(text_splitted, file, ensure_ascii=False, indent=4)
