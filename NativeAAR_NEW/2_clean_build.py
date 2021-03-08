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
import subprocess
from colorama import init, Fore, Back, Style
import shutil

SETTING_NAME = 'settings.gradle'


def clean_build(projectFolderPath):

    projectFolderName = os.path.basename(projectFolderPath)
    print("folder name = " + projectFolderName)

    command_clean = "cd " + os.path.basename(projectFolderPath) + " && gradlew.bat clean"
    os.system(command_clean)

    command_release = "cd " + os.path.basename(projectFolderPath) + " && gradlew.bat assembleRelease"
    os.system(command_release)
    # os.system(command)
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
                clean_build(head)

    os.system("pause")

    return


if __name__ == "__main__":
    logic()
