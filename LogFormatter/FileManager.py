#!/usr/local/bin/python3
# coding: utf-8

###
# FileManager.py
# 
# 
###

#--- モジュールのインポート ---#
import sys
import os

#--- 変数宣言 ---#
curScript = sys.argv[0]


#--- 指定ディレクトリ内に指定拡張子のファイルがあるのかチェックする ---#
# dirPath:指定ディレクトリパス
# extension:指定ファイル拡張子
def GetFilesList(dirPath, extension):
    #--- 変数宣言 ---#
    filesList = []

    for file in os.listdir(dirPath):
        if file.endswith(extension):
            filePath = os.path.join(dirPath, file)
            filesList.append(filePath)
    return filesList

#--- main関数 ---#
def main():
    print("Youは本スクリプト：{}を直接実行しました".format(curScript))

if __name__ == "__main__":
    main()
