# 문제 10: 영단어 퀴즈
words = {
    "사과": "apple",
    "바나나": "banana",
    "학교": "school"
}
score = 0
for i in words:
    answer = input(i + "를 영어로 하면?")
    if answer == words[i]:
        print("정답입니다! 👍")
        score += 1
    else:
        print("아쉬워요," + words[i] + "입니다.")
print(score)
