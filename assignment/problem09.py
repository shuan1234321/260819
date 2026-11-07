# 문제 09: 편의점 메뉴 가격 조회
menu = {
    "삼각김밥": 1200,
    "바나나우유": 1700,
    "컵라면": 1500,
    "샌드위치": 2500
}

order = input("먹고 싶은 메뉴를 입력하세요: ")

found = False

for item in menu:
    if item == order:
        print(item + "은(는) " + str(menu[item]) + "원입니다.")
        found = True

if found == False:
    print("해당 메뉴는 판매하지 않습니다.")