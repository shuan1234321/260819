# 문제 11: 영화 데이터 분석
movies = [
    {"title": "인사이드 아웃 2", "genre": "애니메이션", "rating": 9.0, "views": 1500},
    {"title": "파묘", "genre": "미스터리", "rating": 8.2, "views": 2100},
    {"title": "베테랑 2", "genre": "액션", "rating": 7.5, "views": 1800},
    {"title": "스즈메의 문단속", "genre": "애니메이션", "rating": 8.8, "views": 1300},
    {"title": "범죄도시 4", "genre": "액션", "rating": 8.1, "views": 2500}
]

print("[평점 8.5 이상 영화]")
for movie in movies:
    if movie["rating"] >= 8.5:
        print("- " + movie["title"])
total = 0
for movie in movies:
    if movie["genre"] == "애니메이션":
        total = total + movie["views"]
print("애니메이션 총 조회수: " + str(total) + "회")
miews = 0
mitle = ""
for movie in movies:
    if movie["views"] > miews:
        miews = movie["views"]
        mitle = movie["title"]
print("최다 조회수 영화: " + mitle + " (" + str(miews) + "회)")