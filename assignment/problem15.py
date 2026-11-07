# 문제 15: 업다운 숫자 맞히기
import random

secret = random.randint(1, 100)
count = 0

while True:
    guess = int(input("1~100 사이 숫자를 맞혀보세요: "))
    count = count + 1

    if guess < secret:
        print("UP!")
    elif guess > secret:
        print("DOWN!")
    else:
        print("정답입니다! 축하합니다!")
        print(count, "번 만에 맞혔어요.")
        break