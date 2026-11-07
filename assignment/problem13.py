# 문제 13: 로또 번호 생성기
import random

lotto = [0, 0, 0, 0, 0, 0]  # 6칸을 미리 0으로 채워둔 리스트
count = 0  # 지금까지 채운 개수

while count < 6:
    num = random.randint(1, 45)
    # 여기에 중복 검사 및 번호 저장 코드를 작성하세요
    is_duplicate = False
    for n in lotto:
        if n == num:
            is_duplicate = True

    if is_duplicate == False:
        lotto[count] = num
        count += 1

print("오늘의 행운 번호 6개:", lotto)