#!/usr/local/bin/python3
# coding: utf-8

###
# /* SingleBarhChartPlotter.py */
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
    inputFile = 'TemperatureData.csv'
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
    plt.rcParams['axes.axisbelow']  = True   # grid線を後ろに
    plt.rcParams['xtick.direction'] = 'out'
    plt.rcParams['ytick.direction'] = 'out'
    plt.rcParams['font.family']     = 'Meiryo'

    #--- オブジェクト生成 ---#
    # inch -> cm 変換式
    cm = 1 / 2.54
    fig, ax = plt.subplots(figsize=(16*cm, 10*cm))
    
    #--- 23-Apl のデータのみ抽出 ---#
    target_date = '23-Apr'
    
    if target_date not in date:
        print(f"Error: {target_date} not found in data.")
        return
    
    idx = date.index(target_date)  # 23-Apl のインデックス取得
    
    # 都市とその23-Aplのデータを抽出
    cities_data = {
        '京都': kyoto[idx],
        '札幌': sapporo[idx],
        '東京': tokyo[idx],
        # '仙台': sendai[idx],
        '名古屋': nagoya[idx],
        # '大阪': osaka[idx],
        # '金沢': kanazawa[idx],
        '広島': hiroshima[idx],
        # '高松': takamatsu[idx],
        '博多': hakata[idx],
        # '那覇': naha[idx]
    }

    # 系列数を計算
    city_names = list(cities_data.keys())
    n = len(cities_data)                    # 都市数
    
    bar_height = 0.7

    # 棒グラフをプロット（labelを使用）
    for i, (city, temp) in enumerate(cities_data.items()):
        ax.barh(i, temp, height=bar_height, label=city)

        # 各棒の横に値を表示
        ax.text(temp + 0.2, i, f'{temp:.1f}', va='center')

    #--- 書式設定・出力設定 ---#
    # 目盛線, 補助線
    ax.grid(which='major', linestyle='dashed')  # grid線表示設定

    # 各種名称設定
    ax.set_xlabel("平均気温(2023年4月) [°C]")   # X軸ラベル名称
    ax.set_ylabel("都道府県")                   # Y軸ラベル名称
    ax.set_yticks(np.arange(0, len(city_names)))
    ax.set_yticklabels(city_names)

    # y軸の順序を反転
    ax.invert_yaxis()

    # 軸メモリ設定
    xMin = 0
    xMax = 20
    xTicksOffset = 1
    ax.set_xticks(np.arange(xMin, xMax + 1, xTicksOffset))  # X軸メモリ刻み
    ax.set_xlim(xMin, xMax)                                 # X軸表示範囲

    # 凡例設定
    ax.legend(
                ncol=n, 
                frameon=False, 
                shadow=False, 
                loc='upper center', 
                bbox_to_anchor=(0.5, -0.18)
                )

    # レイアウトを調整
    fig.tight_layout()

    # グラフ出力
    outputPath = os.path.join(exeFileDir, "SingleBarhChartPlotter.pdf")
    plt.savefig(outputPath, bbox_inches="tight", pad_inches=0.05)
    plt.show()

if __name__ == "__main__":
    main()