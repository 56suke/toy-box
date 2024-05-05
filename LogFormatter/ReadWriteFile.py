#!/usr/local/bin/python3
# coding: utf-8

###
# ReadWriteFile
# ファイルの読書用スクリプト
# 
###

#--- モジュールのインポート ---#
import sys
import csv
import openpyxl

#--- 変数宣言 ---#
curScript = sys.argv[0]


#=== .txtファイル処理ブロック ===#
#--- .txtファイルの読込 ---#
# inputFile:入力'.txtファイル'(.txtファイルまでのパス)
def ReadTxtFile(inputFile):
    #--- 変数宣言 ---#

    #--- .txtファイルの中身を取得 ---#
    with open(inputFile, 'r') as f:
        allData = f.read()
    return allData


#--- .txtファイルの書込 ---#
# data:出力データ
# outputFile:出力'.txtファイル'(.txtファイルまでのパス)
def WriteTxtFile(data, outputFile):
    #--- 変数宣言 ---#

    #--- .txtファイル出力 ---#
    with open(outputFile, 'w') as f:
        f.write(data)


#=== .csvファイル処理ブロック ===#
#--- .csvファイル読込 ---#
# inputFile:入力'.csvファイル'(.csvファイルまでのパス)
def ReadCsvFile(inputFile):
    #--- 変数宣言 ---#

    #--- .csvファイルの中身をリストとして取得 ---#
    with open(inputFile, 'r') as f:
        data = csv.reader(f)
        listData = list(data)
    return listData


#--- .csv(tsv)ファイル出力 ---#
# data:出力データ
# outputFile:出力'.csvファイル'(.csvファイルまでのパス)
# デリミタはタブ(\t)
def WriteTsvFile(data, outputFile):
    #--- 変数宣言 ---#

    #--- tsvファイル出力 ---#
    with open(outputFile, 'w', newline='') as f:
        writer = csv.writer(f, delimiter='\t')

        # 各業のデータをCSVファイルに書込
        for row in data:
            # 各行のデータをタブで分割してリスト化し、CSVファイルに書込
            writer.writerow(row.split('\t'))


#=== .xlsxファイル処理ブロック ===#
#--- ('\t'区切りの)dataをExcelに新規出力 ---#
# data:出力データ
# outputFile:出力'.xlsxファイル'(.xlsxファイルまでのパス)
def WriteTabSprDataToExcelFile(data, outputFile):
    #--- 変数宣言 ---#

    # 新規ワークブックの作成
    wb = openpyxl.Workbook()
    ws = wb.active

    # 各行のデータをExcelシートに追加
    for row in data:
        # タブで分割してリストに格納
        formattedData = row.split('\t')
        # Excelシートにデータ行を追加
        ws.append(formattedData)

    # Excelファイルを保存
    wb.save(outputFile)

#=== 設定ファイル読込ブロック ===#
#--- 色情報の設定ファイル(csv)を読み込み、辞書型の変数に値をセットし返却するメソッド ---#
# <Parameters>
# inputFile (str)           : 入力'.csvファイル'(.csvまでのパス)
#
# <Returns>
# colorDict(dict)           : 色情報辞書型変数(色名称:色コード)
def ReadColorInfoFile(inputFile):
    #--- 変数宣言 ---#
    colorDict = {}

    with open(inputFile, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            colorName = row['# ColorName']
            colorCode = row['ColorCode']
            colorDict[colorName] = colorCode

    return colorDict

#--- main関数 ---#
def main():
    print("Youは本スクリプト：{}を直接実行しました".format(curScript))

if __name__ == "__main__":
    main()
