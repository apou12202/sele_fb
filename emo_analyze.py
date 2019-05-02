###########################################
#                                         #
#            Analyze love/angry           #
#                                         #
###########################################
import json
import io

A_angry_part = []
A_love_part = []
B_angry_part = []
B_love_part = []

angry_times = []
love_times = []

with io.open("output/CrossAnalyze/Lai1.json", encoding='utf-8') as file:
    lai1 = json.load(file)

    lai1_angry_cnt = len(lai1[0]['怒'])
    lai1_love_cnt = len(lai1[1]['愛心'])
    print(lai1_angry_cnt)
    print(lai1_love_cnt)

    for i in range(lai1_angry_cnt):
        A_angry_part.append(lai1[0]['怒'][i])
    for i in range(lai1_love_cnt):
        A_love_part.append(lai1[1]['愛心'][i])

with io.open("output/CrossAnalyze/Lai2.json", encoding='utf-8') as file1:
    lai2 = json.load(file1)
    lai2_angry_cnt = len(lai2[0]['怒'])
    lai2_love_cnt = len(lai2[1]['愛心'])

    for i in range(lai2_angry_cnt):
        B_angry_part.append(lai2[0]['怒'][i])
    for i in range(lai2_love_cnt):
        B_love_part.append(lai2[1]['愛心'][i])




for i in A_angry_part:
    cnt = 0
    for j in B_angry_part:
        if i == j:
            task = {
                'name': i,
                'times': 2
            }
            cnt += 1
            angry_times.append(task)

    if cnt == 0:
        task = {
            'name': i,
            'times': 1
        }
        angry_times.append(task)

# print(angry_times)

for i in A_love_part:
    cnt = 0
    for j in B_love_part:
        if i == j:
            task = {
                'name': i,
                'times': 2
            }
            cnt += 1
            love_times.append(task)

    if cnt == 0:
        task = {
            'name': i,
            'times': 1
        }
        love_times.append(task)

# print(love_times)

for i in B_angry_part:
    cnt = 0
    for j in range(len(angry_times)):
        if i != angry_times[j]['name']:
            cnt += 1
    if cnt != 0:
        task = {
            'name': i,
            'times': 1
        }
        angry_times.append(task)


for i in B_love_part:
    cnt = 0
    for j in range(len(love_times)):
        if i != love_times[j]['name']:
            cnt += 1
    if cnt != 0:
        task = {
            'name': i,
            'times': 1
        }
        love_times.append(task)




print(angry_times)
print(love_times)
# print(len(A_angry_part) + len(B_angry_part))
# print(len(A_love_part) + len(B_love_part))
# print(len(angry_times))
# print(len(love_times))

with io.open("output/AngryCrossAnalyze.json", 'w', encoding='utf-8') as file:
    json.dump(angry_times, file, ensure_ascii=False, indent=4)

with io.open("output/loveCrossAnalyze.json", 'w', encoding='utf-8') as file:
    json.dump(love_times, file, ensure_ascii=False, indent=4)
