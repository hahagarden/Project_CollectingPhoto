#파일쓰기

data="hello"
with open("C:/git/Project_CollectingPhoto/exercise/test.txt",'w') as f:
    f.write(data)

#파일읽기
with open("C:/git/Project_CollectingPhoto/exercise/test.txt",'r') as fp:
    print(".......................")
    print(fp.read())

