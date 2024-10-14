#!/usr/local/bin/python3
# coding: utf-8

###
# /* PieChartPlotter.py */
# 
# 
###

#--- モジュールのインポート ---#
import sys
import os
import matplotlib.pyplot as plt
import numpy as np

# プロジェクトのルートディレクトリをsys.pathに追加
#sys.path.append(os.path.join(os.path.dirname(__file__), '../../../'))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

#--- 自作モジュールのインポート ---#
from Utility import FileReadWriter, ExcelFileFormatter, FileManager, DataManager

#--- 変数宣言 ---#
curScript = sys.argv[0]

#--- main関数 ---#
def main():

    #--- 変数宣言 ---#
    inputFile = 'Precipitation.csv'
    _, exeFileDir = FileManager.GetExecPath(__file__)
    inputFilePath = os.path.join(exeFileDir, inputFile)

    inputData   = FileReadWriter.ReadCsvFile(inputFilePath, True)
    date        = []
    kyoto       = []
    sapporo     = []
    tokyo       = []
    sendai      = []
    nagoya      = []
    osaka       = []
    kanazawa    = []
    hiroshima   = []
    takamatsu   = []
    hakata      = []
    naha        = []

    for data in inputData[0]:
        date.append(data[0])
        kyoto.append(float(data[1]))
        sapporo.append(float(data[2]))
        tokyo.append(float(data[3]))
        sendai.append(float(data[4]))
        nagoya.append(float(data[5]))
        osaka.append(float(data[6]))
        kanazawa.append(float(data[7]))
        hiroshima.append(float(data[8]))
        takamatsu.append(float(data[9]))
        hakata.append(float(data[10]))
        naha.append(float(data[11]))
    
    #--- rcParams設定 ---#
    #plt.rcParams['axes.axisbelow']  = True   # grid線を後ろに
    #plt.rcParams['xtick.direction'] = 'out'
    #plt.rcParams['ytick.direction'] = 'out'
    plt.rcParams['font.family']     = 'Meiryo'

    #--- オブジェクト生成 ---#
    # inch -> cm 変換式
    cm = 1 / 2.54
    _, ax = plt.subplots(figsize=(12*cm, 12*cm))
    
    #--- グラフの描画設定 ---#
    citiesData = {
        '京都': kyoto,
        '札幌': sapporo,
        '東京': tokyo,
        '仙台': sendai,
        '名古屋': nagoya,
        '大阪': osaka,
        '金沢': kanazawa,
        '広島': hiroshima,
        #'高松': takamatsu,

        '博多': hakata,
        '那覇': naha
    }

    cityNames = list(citiesData.keys())   # 都市名
    
    values = []
    for _, data in citiesData.items():
        for value in data:
            values.append(value)

    #--- 書式設定・出力設定 ---#
    ax.pie(values, labels=cityNames, autopct='%1.1f%%', startangle=90, counterclock=False,
            wedgeprops={'edgecolor':'white'})

    # タイトル設定
    ax.set_title('2023年6月度の都市別降水量の割合', fontsize=16, fontweight='bold')

    # 凡例設定
    ax.legend(
                ncol=int(len(citiesData) / 2),
                frameon=False, 
                shadow=False, 
                loc='upper center', 
                bbox_to_anchor=(0.5, 0)
                )

    # 円グラフを正円にする
    ax.axis('equal')

    # グラフ出力
    outputPath = os.path.join(exeFileDir, "PieChart.pdf")
    plt.savefig(outputPath, bbox_inches="tight", pad_inches=0.05)
    plt.show()

if __name__ == "__main__":
    main()