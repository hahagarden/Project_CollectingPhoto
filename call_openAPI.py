#카카오 이미지 검색 OpenAPI 호출하기

import requests
import json

#이미지 검색
url="https://dapi.kakao.com/v2/search/image"
headers={
    "Authorization" : "KakaoAK cc335daa766cc74b3de1b1c372a6cce8"
}
data={
    "query" : "펭수"
}

#이미지 검색 요청
response=requests.post(url, headers=headers, data=data)
#요청에 실패했다면,
if response.status_code != 200:
    print("error! because", response.json())
else: #성공했다면
    count=0

for image_info in response.json()['documents']:
    print(f"[{count}thj] image_uril =", image_info['image_url'])
    #저장될 이미지 파일명 설정
    count=count+1

