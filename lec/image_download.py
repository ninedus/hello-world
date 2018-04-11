import urllib.request

url = "https://t1.daumcdn.net/daumtop_chanel/op/20170315064553027.png"
imgName = "D:\Workspace\python\daum.png"
imgName2 = "D:\Workspace\python\daum2.png"

urllib.request.urlretrieve(url, imgName)
print("Download completed!")

#urlretrieve() 함수는 파일로 바로 저장하고,
#urlopen() 함수는 파일로 바로 저장하지 않고 메모리에 로딩을 한다.

downImg = urllib.request.urlopen(url).read()

#파일로 저장하는 과정
with open(imgName2, mode = "wb") as f:
    f.write(downImg)

print("Image download completed")
