import requests
import json

with open("url.json", "r", encoding="utf-8") as f:
    url_list = json.load(f)
base_url = url_list[0]["JSON_HOLDER"]

# TODO :: 나중에 여기서 플라스크 API 로컬 백엔드 주소로 바꿔서 테스트 ㄱㄱ~~
# 요청할 URL
url = f"{base_url}/posts/1"

# 요청 헤더 정의 (dict 형태)
headers = {
    # 내가 보내는 데이터 타입이 JSON이라는 뜻
    "Content-Type": "application/json",
}

# GET 요청 + headers 함께 전달
response = requests.get(url, headers=headers)

# 상태 코드 출력
print(response.status_code)  # 정상: 200

# 응답 데이터 출력
print(response.json())
