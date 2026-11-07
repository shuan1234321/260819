# 문제 14: 가위바위보 게임

import random

win = 0
draw = 0
lose = 0

while True:
    user = input("가위, 바위, 보 중 하나 입력 (종료: 그만): ")
    if user == "그만":
        break
    computer = random.randint(1, 3)
    if computer == 1:
        com = "가위"
    elif computer == 2:
        com = "바위"
    else:
        com = "보"

    print("컴퓨터:", com)

    if user == com:
        print("비겼습니다!")
        draw =+ 1
    elif (user == "가위" and com == "보") or (user == "바위" and com == "가위") or (user == "보" and com == "바위"):
        print("이겼습니다!")
        win =+ 1
    else:
        print("졌습니다!")
        lose =+ 1

print("최종 전적:", win, "승", draw, "무", lose, "패")
















