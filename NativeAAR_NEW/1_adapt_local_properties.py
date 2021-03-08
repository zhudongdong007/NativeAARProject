#!/usr/bin/python
# -*- coding: UTF-8 -*-


import os
from colorama import init, Fore, Back, Style


PC_LOCAL_SDK_DIR = r'sdk.dir=D\:\\Android\\SDK\\Android_Studio'
PC_LOCAL_NDK_DIR = r'ndk.dir=D\:\\Android\\SDK\\Android_Studio\\ndk-bundle'



SETTING_NAME = 'settings.gradle'
LOCAL_PROPERTIES = 'local.properties'


def adapt_local_properties(projectFolder):
    # print(projectFolder)

    # remove the original file
    localPropertiesPath = projectFolder + os.path.sep + LOCAL_PROPERTIES
    if (os.path.exists(localPropertiesPath)):
        os.remove(localPropertiesPath)

    fileExist = False

    if not fileExist:
        with open(projectFolder + os.path.sep + LOCAL_PROPERTIES, 'w') as infile:
            infile.write(PC_LOCAL_SDK_DIR + '\n')

    return


# 函数的主要逻辑
def logic():
    # 初始化，并且设置颜色设置自动恢复
    # 如果未设置autoreset=True，需要使用如下代码重置终端颜色为初始设置
    # print(Fore.RESET + Back.RESET + Style.RESET_ALL)  autoreset=True
    init(autoreset=True)

    # 获取当前文件夹的路径
    currentFolderPath = os.path.dirname(os.path.realpath(__file__))
    print("the current folder path : " + currentFolderPath + "\n")

    # 查找这个路径下面，所有的项目
    for root, dirs, files in os.walk(currentFolderPath):
        for file in files:
            fileRealPath = root + os.path.sep + file
            if fileRealPath.endswith(SETTING_NAME):
                head, tail = os.path.split(fileRealPath)
                print(Fore.GREEN + "Project path = " + head)
                adapt_local_properties(head)


    os.system("pause")


if __name__ == "__main__":
    logic()
