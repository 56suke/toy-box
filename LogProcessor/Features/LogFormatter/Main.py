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
from tkinter import Tk, messagebox


# プロジェクトのルートディレクトリをsys.pathに追加
#sys.path.append(os.path.join(os.path.dirname(__file__), '../../../'))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

#--- 自作モジュールのインポート ---#
from Utility import FileReadWriter, ExcelFileFormatter, FileManager, DataManager

#--- 変数宣言 ---#
curScript = sys.argv[0]
#inputFile = sys.argv[1]

# 入力データファイルディレクトリ名称
INPUTDATA_DIR_NAME = "InputData"
# 入力データファイル名称
INPUT_FILE_NAME = "input.txt"
# 設定ファイルディレクトリ名称
SETTING_DIR_NAME = "Settings"
# ヘッダ文字列定数
HEADER_STR_LIST = ['# Date', 'Time', 'Data1', 'Data2', 'Color', 'Direction', 'Value']


#--- main関数 ---#
def main():
    #--- 変数宣言 ---#

    #--- 実行ファイルパスを取得 ---#
    _, exeFileDir = FileManager.GetExecPath(__file__)
    inputFilePath = os.path.join(exeFileDir, INPUT_FILE_NAME)

    #--- ファイル統合処理 ---#
    # 入力データディレクトリパス
    inputDataDirPath = os.path.join(exeFileDir, INPUTDATA_DIR_NAME)
    # 入力データディレクトリパスから入力データファイルリスト生成
    inputFileList = FileManager.GetFilesList(inputDataDirPath, '.txt')
    # データの統合
    mergedData = FileReadWriter.MergeTxtFiles(inputFileList)
    # 統合データを.txtファイルとして出力
    outputInputFile = os.path.join(exeFileDir, INPUT_FILE_NAME)
    FileReadWriter.WriteTxtFile(mergedData, outputInputFile)

    #--- 入力ファイル名称取得 ---#
    fileName = os.path.splitext(os.path.basename(INPUT_FILE_NAME))[0]
    #--- 出力ファイル名称設定 ---#
    outputExcelFile = fileName + '.xlsx'
    outputExcelFile = os.path.join(exeFileDir, outputExcelFile)

    #--- ファイル読込 ---#
    rowData = FileReadWriter.ReadTxtFile(inputFilePath)
    #--- 時系列にソート ---#
    sortData = DataManager.FormatAndSortDateData(rowData, 0, 1)
    #--- ファイル出力 ---#
    FileReadWriter.WriteTabSprDataToExcelFile(sortData, outputExcelFile)


    #=== Excel編集ブロック ===#
    #--- ヘッダ挿入 ---#
    ExcelFileFormatter.InsertHeader(outputExcelFile, HEADER_STR_LIST)
    #--- セル列幅調整 ---#
    ExcelFileFormatter.AdjustColWidth(outputExcelFile)
    #--- セル行高設定 ---#
    ExcelFileFormatter.SetRowHeight(outputExcelFile, 25)
    #--- フォント設定 ---#
    ExcelFileFormatter.SetDesignedFont(outputExcelFile, "Arial")
    #--- ヘッダ行の文字を太字に設定する ---#
    ExcelFileFormatter.SetHeaderFontBold(outputExcelFile)
    #--- ヘッダ行文字列を上下中央揃えに設定する ---#
    ExcelFileFormatter.SetHeaderAlignment(outputExcelFile)
    #--- フィルタ適用 ---#
    ExcelFileFormatter.ApplyFilter(outputExcelFile, 1, 10)
    #--- ウィンドウ枠の固定 ---#
    ExcelFileFormatter.UseFreezePanes(outputExcelFile, "A2")

    #--- カラムの値に応じて行のセルの色を設定 ---#
    # 色情報設定ファイルディレクトリパス
    setDirPath = os.path.join(exeFileDir, SETTING_DIR_NAME)
    colorSetFilePath = os.path.join(setDirPath, "ColorsInfo.csv")
    # 色情報を設定ファイルから取得
    colorInfo = FileReadWriter.ReadColorInfoFile(colorSetFilePath)
    # 行のセルの色を設定
    ExcelFileFormatter.SetRowColors(outputExcelFile, colorInfo, 4, 10)

    #--- messageBox表示 ---#
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    messagebox.showinfo('通知', 'フォーマット処理が完了しました')
    root.destroy()

if __name__ == "__main__":
    main()
