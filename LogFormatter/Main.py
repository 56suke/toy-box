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
import DataOperate

#--- 変数宣言 ---#
curScript = sys.argv[0]
#inputFile = sys.argv[1]

inputFile = "input.txt"

# 設定ファイルディレクトリ名称
SETTING_DIR_NAME = "Settings"

# ヘッダ文字列定数
HEADER_STR_LIST = ['# Date', 'Time', 'Data1', 'Data2', 'Color', 'Direction', 'Value']

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
    editData = rowData.strip().split('\n')
    #--- 時系列にソート ---#
    sortData = DataOperate.SortDateData(editData)
    #--- ファイル出力 ---#
    ReadWriteFile.WriteTabSprDataToExcelFile(sortData, outputExcelFile)


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

    #--- カラムの値に応じて行のセルの色を設定 ---#
    # 色情報設定ファイルパス
    setDirPath = os.path.join(exeFileDir, SETTING_DIR_NAME)
    colorSetFilePath = os.path.join(setDirPath, "ColorsInfo.csv")

    # 色情報を設定ファイルから取得
    colorInfo = ReadWriteFile.ReadColorInfoFile(colorSetFilePath)

    # 行のセルの色を設定
    EditExcelFile.SetRowColors(outputExcelFile, colorInfo, 4, 10)


if __name__ == "__main__":
    main()
