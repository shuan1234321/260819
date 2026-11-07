# 문제 08: 구구단 (2~9단)
for i in range(2, 10):            # 2단부터 9단까지
    print(i, "단")                 # 단 제목
    for j in range(1, 10):        # 1부터 9까지 곱하기
        print(i, "x", j, "=", i * j)
    print()