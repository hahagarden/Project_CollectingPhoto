#이미지가 있는 image_url을 통해 file_name 파일로 저장하는 함수

def save_image(image_url, file_name):
    img_response=requests.get(image_url)
    #요청에 성공했다면,
    if img_response.status_code == 200:
        #파일 저장
        with open("file_name",'wb') as f:
            f.write(img_response.content)

        