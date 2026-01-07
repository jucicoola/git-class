import json
import requests


# -------------------------------
# 1) API 호출
# -------------------------------

# 요청할 API 주소
# jsonplaceholder는 연습용(가짜) API 서버
# /posts/1 은 id가 1인 게시글 하나를 의미
url = "https://jsonplaceholder.typicode.com/posts/1"


# GET 요청 보내기
# → 서버에 "id가 1인 게시글 데이터를 주세요" 라고 요청
response = requests.get(url)


# -------------------------------
# 2) JSON → 파이썬 데이터 변환
# -------------------------------

# 서버가 JSON 형식으로 응답한 데이터를
# 파이썬에서 사용할 수 있도록 변환
# 결과는 하나의 게시글 정보가 담긴 딕셔너리(dict)
post = response.json()


# -------------------------------
# 3) JSON 파일로 저장
# -------------------------------

# post1.json 파일을 "쓰기(w)" 모드로 열기
# encoding="utf-8" → 한글이 깨지지 않도록 설정
# with 문을 사용하면 파일을 자동으로 닫아줌
with open("post1.json", "w", encoding="utf-8") as f:
    
    # json.dump()
    # → 파이썬 딕셔너리(post)를 JSON 형식으로 파일에 저장
    # ensure_ascii=False → 한글을 유니코드(\uXXXX)로 바꾸지 않음
    # indent=2 → 들여쓰기를 적용해 사람이 읽기 쉽게 저장
	    json.dump(post, f, ensure_ascii=False, indent=2)


# 파일 저장이 끝났음을 알려주는 메시지 출력
print("🎉 post1.json 파일 저장 완료!")