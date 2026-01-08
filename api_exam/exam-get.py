import requests
import json

with open("url.json", "r", encoding="utf-8") as f :
    url_list = json.load(f)
base_url = url_list[0]["JSON_HOLDER"]

# 요청할 URL
url = f"{base_url}/posts/1"

# GET 요청 보내기
response = requests.get(url)

# 응답 객체 출력 (상태코드 확인용)
print(response)          # <Response [200]>

# 상태코드만 보고 싶을 때
print(response.status_code)  # 200

# JSON 응답 내용 확인
print(response.json())


# 모든 post 내용 get 하기
full_url = f"{base_url}/posts"
full_response = requests.get(full_url)
print(full_response)
print(full_response.status_code)
print(full_response.json())