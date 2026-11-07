# 문제 06: 비밀번호 확인
password = "python123"

while True:
    any_input = input("비밀번호를 입력하세요: ")

    if any_input == password:
        print("로그인 성공! 환영합니다.")
        break
    else:
        print("비밀번호가 틀렸습니다. 다시 입력하세요.")