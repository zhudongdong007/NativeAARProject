#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@author:zdd5254
@file: clear_files.py
@time: 2019/10/31
@contact: zdd5254@arcsoft.com

"""

import os
import platform
from colorama import init, Fore, Back, Style
import shutil

SETTING_NAME = 'settings.gradle'

DELETE_FILES = [".iml", "local.properties", ".DS_Store"]
DELETE_FOLDERS = [".gradle", ".idea", "build", "captures", ".externalNativeBuild", ".cxx"]

EXTRAL_DIR = 'projectDir'


def clear(folderPath):
    # matches = parse_gitignore(folderPath + os.path.sep + ".gitignore")
    #
    # if matches(folderPath + os.path.sep + "settings.gradle"):
    #     print("MATCH")

    for root, dirs, files in os.walk(folderPath):
        for file in files:
            fileRealPath = root + os.path.sep + file
            for delete_file_index in range(len(DELETE_FILES)):
                if fileRealPath.endswith(DELETE_FILES[delete_file_index]):
                    os.remove(fileRealPath)
                    print("delete file : " + fileRealPath)

        for dir in dirs:
            folderRealPath = root + os.path.sep + dir
            for delete_folder_index in range(len(DELETE_FOLDERS)):
                if folderRealPath.endswith(DELETE_FOLDERS[delete_folder_index]):
                    shutil.rmtree(folderRealPath, ignore_errors=True)
                    print("delete folder : " + folderRealPath)

    return


def analysisSetting(settingPath, extradirlist):
    fileHandle = open(settingPath)
    fileLines = fileHandle.readlines()
    for i in range(0, fileLines.__len__()):
        line = fileLines[i]
        if line.find(EXTRAL_DIR) != -1:
            print(Fore.GREEN + "dir line: " + line.strip())
            extraName = line.split("'")[-2].strip()
            print("split str = " + extraName)

            # 判断当前的系统是Linux、Windows、还是Darwin，其中Darwin就是MAC
            # Linux系统会左右多一个单引号
            if 'Windows' in platform.system():
                extraName = extraName.replace("/", os.path.sep)

            head, tail = os.path.split(settingPath)

            extraFullPath = head + os.path.sep + extraName
            print("extraFullPath = " + extraFullPath)
            extradirlist.append(extraFullPath)
    fileHandle.close()

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

    listExtralProjectDir = []

    # 查找这个路径下面，所有的项目
    for root, dirs, files in os.walk(currentFolderPath):
        for file in files:
            fileRealPath = root + os.path.sep + file
            if fileRealPath.endswith(SETTING_NAME):
                analysisSetting(fileRealPath, listExtralProjectDir)
                head, tail = os.path.split(fileRealPath)
                print(Fore.GREEN + "Project path = " + head)
                clear(head)

    for index in range(len(listExtralProjectDir)):
        clear(listExtralProjectDir[index])

    os.system("pause")

    return


if __name__ == "__main__":
    logic()
