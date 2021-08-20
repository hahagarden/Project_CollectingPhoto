import requests  #import Library after cmd pip install requests

print("////////////")

#이미지가 있는 url 주소
url="http://search1.kakaocdn.net/argon/600x0_65_wr/ImZk3b2X1w8" 

#해당 url로 서버에게 요청
img_response=requests.get(url) 

#요청에 성공했다면,
if img_response.status_code==200:
    #print(img_response.content)

    print("============[이미지 저장]============")
    with open("test.jpg","wb") as f:  #wb 바이너리 형식을 쓰는 모드
        f.write(img_response.content)  #img_response.content는 jpeg가 binary 형태로 값이 들어있음. jpeg binary 데이터를 파일로 저장하면 이미지 현시

