#!/usr/local/bin/python3
# coding: utf-8

###
# /* NestedPieChartPlotter.py */
# 
# 
###

#--- モジュールのインポート ---#
import sys
import os
import matplotlib.pyplot as plt

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
    plt.rcParams['font.family'] = 'Meiryo'

    #--- オブジェクト生成 ---#
    # inch -> cm 変換式
    cm = 1 / 2.54
    _, ax = plt.subplots(figsize=(12*cm, 12*cm))
    
    #--- グラフの描画設定 ---#
    citiesData = {
        '京都': kyoto,
        #'札幌': sapporo,
        '東京': tokyo,
        #'仙台': sendai,
        #'名古屋': nagoya,
        #'大阪': osaka,
        #'金沢': kanazawa,
        #'広島': hiroshima,
        #'高松': takamatsu,
        '博多': hakata,
        #'那覇': naha
    }

    # 外側の円（都市ごとの合計降水量）
    outer_values = [sum(kyoto), sum(tokyo), sum(hakata)]
    total_precipitation = sum(outer_values)
    outer_labels = [f"{city}: {value / total_precipitation * 100:.1f}%" for city, value in zip(['京都', '東京', '博多'], outer_values)]

    # 内側の円（各月の降水量）
    inner_values = kyoto + tokyo + hakata
    months = ['1月', '2月', '3月', '1月', '2月', '3月', '1月', '2月', '3月']

    lRadValue   = 1
    wValue      = 0.35
    sRadValue   = lRadValue - wValue

    # 外側の円（都市ごとの合計降水量）
    wedges_outer = ax.pie(
        outer_values, labels=outer_labels, radius=lRadValue, pctdistance=0.85, startangle=90, counterclock=False,
        wedgeprops={'edgecolor': 'white', 'width': wValue},  # widthを設定
    )[0]

    # 内側の円（各月の降水量）
    wedges_inner = ax.pie(
        inner_values, labels=months, radius=sRadValue, startangle=90, counterclock=False,
        wedgeprops={'edgecolor': 'white', 'width': wValue}
    )[0]

    # 内側の円の色を外側の色に合わせる
    for i, inner_wedge in enumerate(wedges_inner):
        outer_wedge_color = wedges_outer[i // 3].get_facecolor()
        inner_wedge.set_facecolor(outer_wedge_color)
        
        # 透明度を設定
        if i % 3 == 0:  # 1月
            inner_wedge.set_alpha(0.9)
        elif i % 3 == 1:  # 2月
            inner_wedge.set_alpha(0.6)
        else:  # 3月
            inner_wedge.set_alpha(0.3)

    # タイトル設定
    ax.set_title('2023年1-3月度の都市別降水量の割合', fontsize=16, fontweight='bold')

    # 円グラフを正円にする
    ax.axis('equal')

    # グラフ出力
    outputPath = os.path.join(exeFileDir, "NestedPieChart.pdf")
    plt.savefig(outputPath, bbox_inches="tight", pad_inches=0.05)
    plt.show()

if __name__ == "__main__":
    main()