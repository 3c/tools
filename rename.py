#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import re

workPath = os.getcwd()
print workPath

# 自定义的必须忽略 
customFilterList = [
'中英双字幕',
'国语中字',
'6v电影'
] 


# 通用规则
customFilter = "(\[.*\])|(\【.*\】)|(\d{3,4}p)|(bd)|(hd)|(\.)"

# 添加自定义的规则
for str in customFilterList:
	customFilter=customFilter+"|("+str+")"

# print "customFilter= " + customFilter

# 遍历当前目录
for fileName in os.listdir(workPath):
	if(os.path.isfile(fileName)):
		# 先把后缀名取出来。之后再拼上
		fileSuffix = os.path.splitext(fileName)[1] 
		afterFileName =  re.sub(customFilter, "", os.path.splitext(fileName)[0],0,re.I)
		newFileName = afterFileName+fileSuffix
		print "newFileName  : ", newFileName
		os.rename(fileName, newFileName)



