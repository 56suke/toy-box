#!/usr/local/bin/python3
# coding: utf-8

###
# /* StackedBarhChartPlotter.py */
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

    for data in inputData:
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
    plt.rcParams['axes.axisbelow']  = True   # grid線を後ろに
    plt.rcParams['xtick.direction'] = 'out'
    plt.rcParams['ytick.direction'] = 'out'
    plt.rcParams['font.family']     = 'Meiryo'

    #--- オブジェクト生成 ---#
    # inch -> cm 変換式
    cm = 1 / 2.54
    fig, ax = plt.subplots(figsize=(18*cm, 12*cm))
    
    #--- グラフの描画設定 ---#
    cities_data = {
        '京都': kyoto,
        #'札幌': sapporo,
        #'東京': tokyo,
        #'仙台': sendai,
        #'名古屋': nagoya,
        '大阪': osaka,
        #'金沢': kanazawa,
        #'広島': hiroshima,
        '高松': takamatsu,
        #'博多': hakata,
        #'那覇': naha
    }

    # 系列数を計算
    bar_height = 0.8
    y = range(len(date))

    # 各都市のデータを積み上げ棒グラフとしてプロット
    left = np.zeros(len(date))
    for city, data in cities_data.items():
        bars = ax.barh(y, data, bar_height, label=city, left=left)
        
        # 各バーの中心に数値を表示
        for idx, (bar, value) in enumerate(zip(bars, data)):
            width = bar.get_width()
            ax.text(left[idx] + width / 2, 
                    bar.get_y() + bar.get_height() / 2,  # バーの中心に表示
                    f'{value}', ha='center', va='center')

        left += data  # 下の棒の上に積み上げる

    #--- 書式設定・出力設定 ---#
    # 目盛線, 補助線
    ax.grid(which = 'major', linestyle = 'dashed')      # grid線表示設定

    # 各種名称設定
    ax.set_xlabel("降水量 [mm]")            # X軸ラベル名称
    ax.set_ylabel("年月")                   # Y軸ラベル名称
    ax.set_yticks(np.arange(0, len(date)))
    ax.set_yticklabels(date)

    # y軸の順序を反転
    ax.invert_yaxis()

    # 軸メモリ設定
    xMin = 0
    xMax = 280
    xTicksOffset = 20
    ax.set_xticks(np.arange(xMin, xMax + 1, xTicksOffset))  # X軸メモリ刻み
    ax.set_xlim(xMin, xMax)                                 # X軸表示範囲

    # 凡例設定
    ax.legend(
                ncol=len(cities_data), 
                frameon=False, 
                shadow=False, 
                loc='upper center', 
                bbox_to_anchor=(0.5, -0.1)
                )

    # レイアウトを調整
    fig.tight_layout()

    # グラフ出力
    outputPath = os.path.join(exeFileDir, "StackedBarhChartPlotter.pdf")
    plt.savefig(outputPath, bbox_inches="tight", pad_inches=0.05)
    plt.show()

if __name__ == "__main__":
    main()