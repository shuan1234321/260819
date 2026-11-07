# 문제 02: 사칙연산 계산기
number1 = float(input("첫번째 숫자를 입력하세요: "))
number2 = float(input("두번째 숫자를 입력하세요: "))
operator = input("연산자를 입력하세요: ")

if operator == "+":
    result = number1 + number2
elif operator == "-":
    result = number1 - number2
elif operator == "*":
    result = number1 * number2
elif operator == "/":
    if number2 == 0:
        result = "0으로 나눌 수 없습니다"
    else:
        result = number1 / number2
else:
    result = "잘못된 연산자입니다"
print(result)