import os;
import shutil;

#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# clean build dir in android project

# clean dir
def deleteDirs(path , delname="build"):
    dirs = os.listdir(path)
    for dic in dirs:
        if os.path.isdir(os.path.join(path,dic)):
        	if dic == delname:
        		print(os.path.join(path,dic))
        		shutil.rmtree(os.path.join(path,dic))
        	else:
        		deleteDirs(os.path.join(path,dic),delname)
        
        	
# del path
PATH = "D:\\android\\workspace" 
deleteDirs(PATH)