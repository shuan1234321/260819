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
if var1 == var2:
    print("var1과 var2가 같습니다.")
if var1 < var2:
    print("var2가 더 큽니다")


print("=====================")
print("1. 게임 시작")
print("2. 랭킹 확인")
print("0. 게임종료")
print("=====================")
user_input = input("원하는 동작을 입력하세요")

if user_input == "1":
    print("게임을 시작합니다.")