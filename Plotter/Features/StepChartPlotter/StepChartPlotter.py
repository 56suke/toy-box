#!/usr/local/bin/python3
# coding: utf-8

###
# /* StepChartPlotter.py */
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
    inputFile = 'StepPlotData.csv'
    _, exeFileDir = FileManager.GetExecPath(__file__)
    inputFilePath = os.path.join(exeFileDir, inputFile)

    inputData = FileReadWriter.ReadCsvFile(inputFilePath, headerSkip=True)
    months = []
    num1   = []
    num2   = []

    for data in inputData[0]:
        months.append(int(data[0]))
        num1.append(int(data[1]))
        num2.append(int(data[2]))
    
    #--- rcParams設定 ---#
    plt.rcParams['axes.axisbelow']  = True   # grid線を後ろに
    plt.rcParams['xtick.direction'] = 'out'
    plt.rcParams['ytick.direction'] = 'out'
    plt.rcParams['font.family']     = 'Meiryo'

    #--- オブジェクト生成 ---#
    # inch -> cm 変換式
    cm = 1 / 2.54
    fig, ax = plt.subplots(figsize=(16*cm, 12*cm))

    # ステッププロット描画
    ax.step(months, num1, label='A')
    ax.step(months, num2, label='B')

    #--- 書式設定・出力設定 ---#
    # 目盛線, 補助線
    ax.grid(which='major', linestyle='dashed')  # grid線表示設定

    # 各種名称設定
    ax.set_xlabel("月")         # X軸ラベル名称
    ax.set_ylabel("販売数量")    # Y軸ラベル名称

    # 軸メモリ設定
    xMin = 1
    xMax = 12
    yMin = 0
    yMax = 100
    xTicksOffset = 1
    yTicksOffset = 5

    ax.set_xticks(np.arange(xMin, xMax + 1, xTicksOffset))  # X軸メモリ刻み
    ax.set_yticks(np.arange(yMin, yMax + 1, yTicksOffset))  # Y軸メモリ刻み
    ax.set_xlim(xMin, xMax)                                 # X軸表示範囲
    ax.set_ylim(yMin, yMax)                                 # Y軸表示範囲

    # タイトル設定
    ax.set_title('各月毎の販売数(ステッププロット)', fontweight='bold')

    # 凡例設定
    ax.legend(
                #fontsize='small',
                markerscale=2, 
                ncol=2, 
                #columnspacing=0.2, 
                #handletextpad=0, 
                frameon=False, 
                shadow=False, 
                loc='upper center', 
                bbox_to_anchor=(0.5, -0.15)
                )

    # レイアウトを調整
    fig.tight_layout()

    # グラフ出力
    outputPath = os.path.join(exeFileDir, "StepChartPlotter.pdf")
    plt.savefig(outputPath, bbox_inches="tight", pad_inches=0.05)
    plt.show()

if __name__ == "__main__":
    main()