import cv2
import os
from tqdm import tqdm

path = './faceImage/mask/'

# 중복 검사할 이미지 path
# 이미지 지워지지 않습니다 print만 해주는데, 나중에 지울거면 os.remove 같은 지우는 프로그램 만들면됩니당

lid = os.listdir(path)
dic = {}

# duplication Print part
resizeShape = (4,4)
for l in lid:
    img = cv2.imread(path+l)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, resizeShape, interpolation=cv2.INTER_LINEAR)
    img = img.flatten()
    try:
        dic[str(img)] += "____"+path+l
        print(str(dic[str(img)]).split('____'))
    except:
        dic[str(img)] = path+l

# duplication Remove part
for d in dic.values():
    paths = d.split('____')
    if len(paths)>1:
        for p in paths[1:]:
            os.remove(p)
            print(f'{p} is removed')
        