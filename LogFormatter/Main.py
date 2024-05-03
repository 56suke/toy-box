#!/usr/local/bin/python3
# coding: utf-8

###
# Mainスクリプト
# 
# 
###

#--- モジュールのインポート ---#
import sys
import os

#--- 自作モジュールのインポート ---#
import ReadWriteFile
import EditExcelFile

#--- 変数宣言 ---#
curScript = sys.argv[0]
#inputFile = sys.argv[1]

inputFile = "input.txt"

# ヘッダ文字列定数
HEADER_STR_LIST = ['# Date', 'Time', 'Data1', 'Data2', 'Data3', 'Data4', 'Data5']

#--- 実行ファイルパスを取得 ---#
def GetExeFilePath():
    # PyInstallerが生成した一時フォルダ内で実行されている場合
    # sys.executable が実行可能ファイルパスを返却
    if getattr(sys, 'frozen', False):
        applicationPath = os.path.abspath(sys.executable)
    else:
        # スクリプトが直接Pythonインタプリタで実行されている場合
        # 通常のPythonスクリプトとして実行されている場合のファイルパス
        applicationPath = os.path.abspath(__file__)
    
    return applicationPath


#--- main関数 ---#
def main():
    #--- 変数宣言 ---#

    #--- 実行ファイルパスを取得 ---#
    exeFilePath = GetExeFilePath()
    exeFileDir = os.path.dirname(exeFilePath)

    #--- 入力ファイル名称取得 ---#
    fileName = os.path.splitext(os.path.basename(inputFile))[0]

    #--- 出力ファイル名称設定 ---#
    outputExcelFile = fileName + '.xlsx'
    outputExcelFile = os.path.join(exeFileDir, outputExcelFile)

    #--- ファイル読込 ---#
    rowData = ReadWriteFile.ReadTxtFile(inputFile)
    #--- 前処理 ---#
    EditData = rowData.strip().split('\n')
    #--- ファイル出力 ---#
    ReadWriteFile.WriteTabSprDataToExcelFile(EditData, outputExcelFile)


    #=== Excel編集ブロック ===#
    #--- ヘッダ挿入 ---#
    EditExcelFile.InsertHeader(outputExcelFile, HEADER_STR_LIST)
    #--- セル列幅調整 ---#
    EditExcelFile.AdjustColWidth(outputExcelFile)
    #--- セル行高設定 ---#
    EditExcelFile.SetRowHeight(outputExcelFile, 25)
    #--- フォント設定 ---#
    EditExcelFile.SetDesignedFont(outputExcelFile, "Arial")
    #--- フィルタ適用 ---#
    EditExcelFile.ApplyFilter(outputExcelFile, 1, 10)
    #--- ウィンドウ枠の固定 ---#
    EditExcelFile.UseFreezePanes(outputExcelFile, "A2")


if __name__ == "__main__":
    main()
