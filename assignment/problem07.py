# 문제 07: 3-6-9 게임
for i in range(1, 31):
    clap = 0
    tenth = i // 10
    ones = i % 10

    if ones == 3 or ones == 6 or ones == 9:
        clap = 1
    if tenth == 3 or tenth == 6 or tenth == 9:
        clap = 1

    if clap == 0:
        print(i)
    if clap == 1:
        print("짝")