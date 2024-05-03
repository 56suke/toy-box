#!/usr/local/bin/python3
# coding: utf-8

###
# DataOperte.py
# データ操作を行うためのスクリプト
# 
###

#--- モジュールのインポート ---#
import sys
from datetime import datetime

#--- 変数宣言 ---#
curScript = sys.argv[0]

# 日付と時刻の書式
DATE_FORMAT = '%Y/%m/%d %H:%M:%S.%f'


#--- 時系列データのソート ---#
# data:入力データ
def SortDateData(data):
    #--- 変数宣言 ---#

    
    # データを日付と時刻に基づいてソート
    sortedData = sorted(data, key=lambda x: datetime.strptime(x.split()[0] + ' ' + x.split()[1], DATE_FORMAT))

    """
    # ソートされたデータを出力
    for i in sortedData:
        print(i)
    """

    return sortedData


#--- main関数 ---#
def main():
    print("Youは本スクリプト：{}を直接実行しました".format(curScript))

if __name__ == "__main__":
    main()
