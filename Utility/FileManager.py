#!/usr/local/bin/python3
# coding: utf-8

###
# FileManager.py
# ファイル操作用スクリプト
# 
###

#--- モジュールのインポート ---#
import sys
import os

#--- 変数宣言 ---#
curScript = sys.argv[0]

# 日付と時刻の書式
DATE_FORMAT = '%Y/%m/%d %H:%M:%S.%f'


#--- 実行ファイル及びディレクトリパス(絶対パス)を取得 ---#
def GetExecPath(filePath):
    # PyInstallerが生成した一時フォルダ内で実行されている場合
    # sys.executableが実行可能ファイル及びディレクトリパスを返却
    if getattr(sys, 'frozen', False):
        execFilePath    = os.path.abspath(sys.executable)
        execDirPath     = os.path.dirname(execFilePath)
    # スクリプトが直接Pythonインタプリタで実行されている場合
    # 通常のPythonスクリプトとして実行されている場合のファイル及びディレクトリパス
    else:
        execFilePath = os.path.abspath(filePath)
        execDirPath     = os.path.dirname(execFilePath)
    return execFilePath, execDirPath

#--- 指定ディレクトリ内に指定拡張子のファイルがあるのかチェックする ---#
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
