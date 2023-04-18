'''
Author: HY\harry hy546880109@qq.com
Date: 2023-04-18 15:03:16
LastEditors: HY\harry hy546880109@qq.com
LastEditTime: 2023-04-18 15:03:21
FilePath: \AutomationTest\common\md5_passwd.py
Description: 
'''
import hashlib

def Md5_add(num):
    hs = hashlib.md5()
    hs.update(num.encode(encoding='utf-8'))
    return hs.hexdigest()
    
if __name__ == '__main__':
    md = Md5_add(123456)
    print(md)