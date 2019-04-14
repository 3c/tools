import os;
import hashlib;
import shutil;

# _*_ coding:utf-8 _*_  

src = 'D:\\mycloud\\chen\\cx';
merge = 'E:\\merge';

MAX_FILE_SIZE = 10 * 1024 * 1024

CACHE_FILE_NAME = '.key_map_cache_cx'

def getMd5(file):

    fileSize = os.path.getsize(file)
    fileCacheKey = file + "_"+ str(fileSize)
    if(fileCacheKey in cacheMap):
        return cacheMap[fileCacheKey]
    f = open(file,'rb')
    m = hashlib.md5()
    while True:
        b = f.read(8096)
        if not b :
            break
        m.update(b)
    f.close()

    return m.hexdigest()

dic = {}
cacheMap = {}



def saveLargeFileKey(filePath , key):
    fileSize = os.path.getsize(filePath)
    fileCacheKey = filePath + "_"+ str(fileSize)
   
    if(fileCacheKey in cacheMap):
        return
    if(fileSize > MAX_FILE_SIZE):
        #print(filePath,fileSize ,k," too large , need write cache")
        f = open(CACHE_FILE_NAME,"a+")
        f.write(fileCacheKey+","+key+"\n")
        f.close()

def readCacheMap():
    if(os.path.exists(CACHE_FILE_NAME)):
        f = open(CACHE_FILE_NAME,"r")
        listStr = f.read().splitlines()
        for str in listStr:
            strArr = str.split(",")
            cacheMap[strArr[0]]=strArr[1]
        f.close()

readCacheMap()

# 遍历src
files = os.listdir(src);
fileSize = len(files)

i = 0;

for file in files:
    filePath = os.path.join(src,file);
    key = getMd5(filePath)
    i = i+1
    print(i,"/",fileSize)
    value = [filePath]
    if key in dic:
        value.extend(dic.get(key))
    dic[key] = value


for (k,v) in dic.items():
    if len(v) > 1:
        for index, file in enumerate(v):  
            if index == 0:
                saveLargeFileKey(file,k)
                continue;

            shutil.move(file,os.path.join(merge,os.path.basename(file)))
        print("need move ",k ,v)
    else:
        saveLargeFileKey(v[0],k)


