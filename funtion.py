
movies = [
    {"title": "인사이드 아웃 2", "genre": "애니메이션", "rating": 9.0, "views": 1500},
    {"title": "파묘", "genre": "미스터리", "rating": 8.2, "views": 2100},
    {"title": "베테랑 2", "genre": "액션", "rating": 7.5, "views": 1800},
    {"title": "스즈메의 문단속", "genre": "애니메이션", "rating": 8.8, "views": 1300},
    {"title": "범죄도시 4", "genre": "액션", "rating": 8.1, "views": 2500}
]

def retrieve_rating():
    user_input = float(input("평점 몇 이상의 영화를 조회하시겠습니까?"))
    print("[평점",user_input," 이상 영화]")
    for movie in movies:
        if movie["rating"] > user_input:
            print("- ", movie["title"])
def movie_views():
    total_animation_views = 0
    for movie in movies:
        if movie["genre"] == "애니메이션":
            total_animation_views = total_animation_views + movie["views"]
    print("[애니메이션 장르의 누적조회수]")
    print(total_animation_views)
def max_view():
    max_views = 0
    max_title = ""
    for movie in movies:
        if movie["views"] > max_views:
            max_views = movie["views"]
            max_title = movie["title"]
    print("[최다 조회수의 영화]")
    print(max_title, ":", max_views)

def search_movie_by_title(keyword):
    for movie in movies:
        if movie["title"].find(keyword) >= 0:
           return movie
    return None



def search_movie():
    keyword = input("검색할 영화를 입력하세요")
    movie = search_movie_by_title(keyword)
    print(movie)

def external_api_update_movie():
    return [
        {"title": "인사이드 아웃 2", "genre": "애니메이션", "rating": 8.7, "views": 2000},
        {"title": "왕과 사는 남자", "rating": 9.0, "views": 1693},
        {"title": "오디세이", "rating": 9.2, "views": 1236},
        {"title": "폭설", "genre": "스릴러", "rating": 8.5, "views": 35},
        {"title": "토이 스토리 5", "genre": "애니메이션", "rating": 8.7, "views": 295},
    ]


while True:
    print("====================")
    print("1. 평점 기준 조회")
    print("2. 장르별 누적조회수 조회")
    print("3. 최다 조회수 영화 조회")
    print("4. 영화 검색하기")
    print("0. 종료하기")
    print("====================")

    choice = int(input("Enter your choice:"))

    if choice == 0:
        break
    elif choice == 1:
        retrieve_rating()
    elif choice == 2:
        movie_views()
    elif choice == 3:
        max_view()
    elif choice == 4:
        search_movie()