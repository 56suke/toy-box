#!/usr/local/bin/python3
# coding: utf-8

###
# /* BubbleChartPlotter.py */
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
    inputFile = 'SalesData.csv'
    _, exeFileDir = FileManager.GetExecPath(__file__)
    inputFilePath = os.path.join(exeFileDir, inputFile)

    inputData = FileReadWriter.ReadCsvFile(inputFilePath, True)
    price           = []
    sales           = []
    profitMargin    = []

    for data in inputData:
        price.append(float(data[0]))
        sales.append(float(data[1]))
        profitMargin.append(float(data[2]))
    
    #--- rcParams設定 ---#
    plt.rcParams['axes.axisbelow']  = True   # grid線を後ろに
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.rcParams['font.family']     = 'Meiryo'

    #--- オブジェクト生成 ---#
    # inch -> cm 変換式
    cm = 1 / 2.54
    fig, ax = plt.subplots(figsize=(12*cm, 10*cm))
    
    #--- グラフの描画設定 ---#
    # カラーマップを使用してバブルの色を利益率に基づいて設定
    scatter = ax.scatter(
                price,                              # x軸値 (Price)
                sales,                              # y軸値 (Sales)
                s = np.array(profitMargin) * 50,    # バブルのサイズ（利益率にスケーリング）
                c = profitMargin,                   # 色を利益率に基づいて設定
                cmap='turbo',                       # カラーマップを指定
                alpha = 0.7                         # マーカーの透明度
                )
    
    #--- 書式設定・出力設定 ---#
    ax.grid(which = 'major', linestyle = 'dashed')      # grid線表示設定

    # 各種名称設定
    ax.set_title("Price vs Sales (Bubble Size = Profit Margin)")    # グラフタイトル
    ax.set_xlabel("Price")                                          # X軸ラベル
    ax.set_ylabel("Sales")                                          # Y軸ラベル

    # カラーバーを追加して利益率と色の対応を表示
    cbar = fig.colorbar(scatter)

    cbar.ax.tick_params(direction='out')    # カラーバーの目盛りを外向きに設定
    cbar.set_label('Profit Margin')         # カラーバーのタイトル設定

    # カラーバーの目盛りを詳細に設定
    # 最小値と最大値をカラーバーに表示
    min_profit = np.min(profitMargin)
    max_profit = np.max(profitMargin)
    minValue = 7
    diff = 1

    # カラーバーのメモリを整数刻みに設定
    cbar.set_ticks([min_profit] + list(np.arange(minValue, max_profit - 1, diff)) + [max_profit])

    # カラーバーのラベル設定
    cbar.ax.set_yticklabels([f"{min_profit:.1f}"] + [f"{x:.1f}" for x in np.arange(minValue, max_profit -1, diff)] + [f"{max_profit:.1f}"])

    # 軸メモリ設定
    xMin = 0
    xMax = 100
    yMin = 1500
    yMax = 5500
    xTicksOffset = 10
    yTicksOffset = 500

    ax.set_xticks(np.arange(xMin, xMax + 1, xTicksOffset))      # X軸メモリ刻み
    ax.set_yticks(np.arange(yMin, yMax + 0.01, yTicksOffset))   # Y軸メモリ刻み
    ax.set_xlim(xMin, xMax)                                     # X軸表示範囲
    ax.set_ylim(yMin, yMax)                                     # Y軸表示範囲
        
    # レイアウトを調整
    fig.tight_layout()

    # グラフ出力
    outputPath = os.path.join(exeFileDir, "BubbleChart.pdf")
    plt.savefig(outputPath, bbox_inches="tight", pad_inches=0.05)
    plt.show()

if __name__ == "__main__":
    main()
