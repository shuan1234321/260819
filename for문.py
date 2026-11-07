arr = ["apple", "banana", "cherry"]

print("메뉴 리스트")
for item in arr:
    print(item)

print("------------------")
print("메뉴 리스트")
sale_list = {'apple':1, 'banana':0, 'cherry':3}
for key in sale_list:
    if sale_list[key] == 0:
        print(key, "sold out")
    else:
        print(key, sale_list[key])

for i in range(10):
    print(i)

ex_arr = [num for num in range(10)]
print(ex_arr)
#1.개인별 평규 점수 김철수 nn점 등등
#2. 과목별 최고 득점자
#3. 이름으로 검색해서
class_scores = [ { "name": "김철수", "scores": {"국어": 85, "영어": 90, "수학": 78, "과학": 92} }, { "name": "이영희", "scores": {"국어": 92, "영어": 88, "수학": 95, "과학": 96} }, { "name": "박민수", "scores": {"국어": 76, "영어": 65, "수학": 82, "과학": 70} }, { "name": "정수진", "scores": {"국어": 88, "영어": 94, "수학": 90, "과학": 89} }, { "name": "한동석", "scores": {"국어": 60, "영어": 72, "수학": 65, "과학": 58} } ]

for i in class_scores:
    print(i["name"], (i["scores"]["국어"] + i["scores"]["영어"] + i["scores"]["수학"] + i["scores"]["과학"]) / 4, "점")

for i in ["국어", "영어", "수학", "과학"]:
    best_student = class_scores[0]
    for student in class_scores:
        if student["scores"][i] > best_student["scores"][i]:
            best_student = student
    print(i, "1등:", best_student["name"])

name = input("이름: ")
for i in class_scores:
    if i["name"] == name:
        print(i["name"], i["scores"])