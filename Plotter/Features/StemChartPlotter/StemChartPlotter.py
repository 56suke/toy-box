#!/usr/local/bin/python3
# coding: utf-8

###
# /* StemChartPlotter.py */
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

    inputData, headStr = FileReadWriter.ReadCsvFile(inputFilePath, False)
    dateLabels  = headStr

    # 気温データをリストに変換（文字列からfloat型に変換）
    temperature = [float(temp) for temp in inputData[0]]

    # X軸のインデックスを生成 (0, 1, 2, ...)
    x = np.arange(len(dateLabels))
    
    #--- rcParams設定 ---#
    plt.rcParams['axes.axisbelow']  = True   # grid線を後ろに
    plt.rcParams['xtick.direction'] = 'out'
    plt.rcParams['ytick.direction'] = 'out'
    plt.rcParams['font.family']     = 'Meiryo'

    #--- オブジェクト生成 ---#
    # inch -> cm 変換式
    cm = 1 / 2.54
    fig, ax = plt.subplots(figsize=(16*cm, 10*cm))

    # ステムプロット描画
    ax.stem(x, temperature, use_line_collection=True)

    #--- 書式設定・出力設定 ---#
    # 目盛線, 補助線
    ax.grid(which='major', linestyle='dashed')  # grid線表示設定

    # 各種名称設定
    ax.set_xlabel("都道府県・月")           # X軸ラベル名称
    ax.set_ylabel("平均気温 [°C]")          # Y軸ラベル名称
    ax.set_xticks(x)
    ax.set_xticklabels(dateLabels, rotation=90)  # X軸のラベルを90度回転

    # 軸メモリ設定
    yMin = -10
    yMax = 20
    yTicksOffset = 2
    ax.set_yticks(np.arange(yMin, yMax + 1, yTicksOffset))  # Y軸メモリ刻み
    ax.set_ylim(yMin, yMax)                                 # Y軸表示範囲

    # レイアウトを調整
    fig.tight_layout()

    # グラフ出力
    outputPath = os.path.join(exeFileDir, "StemChartPlotter.pdf")
    plt.savefig(outputPath, bbox_inches="tight", pad_inches=0.05)
    plt.show()

if __name__ == "__main__":
    main()