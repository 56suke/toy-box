#!/usr/local/bin/python3
# coding: utf-8

###
# DataManager.py
# データ操作用スクリプト
# 
###

#--- モジュールのインポート ---#
import sys
from datetime import datetime

#--- 変数宣言 ---#
curScript = sys.argv[0]

# 日付と時刻の書式
DATE_FORMAT = '%Y/%m/%d %H:%M:%S.%f'


#--- 時系列データのフォーマットとソート ---#
# data (List) : 入力データ
# DateとTimeがそれぞれ分けられているデータリストが前提
def FormatAndSortDateData(data, dateIndex, timeIndex):
    #--- 変数宣言 ---#

    # データを日付と時刻に基づいてソート
    sortedData = sorted(data, key=lambda x:datetime.strptime(x.split()[dateIndex] + ' ' + x.split()[timeIndex], DATE_FORMAT))
    return sortedData


#--- 時系列データのフォーマットとソート ---#
# data (List) : 入力データ
# DateTimeと既にフォーマット済のデータリストが前提
def SortDateData(data, dateTimeIndex):
    #--- 変数宣言 ---#

    # データを日付と時刻に基づいてソート
    sortedData = sorted(data, key=lambda x:datetime.strptime(x[dateTimeIndex], DATE_FORMAT))
    return sortedData


#--- main関数 ---#
def main():
    print("Youは本スクリプト：{}を直接実行しました".format(curScript))

if __name__ == "__main__":
    main()
