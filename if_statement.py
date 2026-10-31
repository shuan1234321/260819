if True:
    print("true")
    print("True라면 내부는 모두 수행한다")


if False:
    print("false")
    print("false라면 내무는 모두 수행하지 않습니다")

if False:
    print("true")
    print("True라면 내부는 모두 수행한다")
else:
    print("Else")
    print("위 조건들이 트루 아닐때 수행")

print("ALways")
print("=====================")
score = 70

if score > 80:
    print("A학점입니다.")
elif score > 60:
    print("B학점입니다.")
elif score > 40:
    print("C학점입니다.")
elif score > 20:
    print("D학점입니다.")
else:
    print("낙제입니다.")
print("=====================")


var1 = 1
var2 = 2

if var1 > var2:
    print("var1이 더 큽니다.")
elif var1 == var2:
    print("var1과 var2가 같습니다.")
elif var1 < var2:
    print("var2가 더 큽니다")


print("=====================")
print("1. 게임 시작")
print("2. 랭킹 확인")
print("0. 게임종료")
print("=====================")
user_input = input("원하는 동작을 입력하세요")

if user_input == "1":
    print("게임을 시작합니다.")
elif user_input == "2":
    print("랭킹을 확인합니다")
elif user_input == "0":
    print("게임을 종료합니다")

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