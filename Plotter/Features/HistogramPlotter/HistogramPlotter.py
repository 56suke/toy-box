#!/usr/local/bin/python3
# coding: utf-8

###
# /* HistogramPlotter.py */
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
    inputFile = 'final_dataset_BFP.csv'
    exeFilePath = FileManager.GetExecFilePath(__file__)
    exeFileDir = os.path.dirname(exeFilePath)
    inputFilePath = os.path.join(exeFileDir, inputFile)

    inputData = FileReadWriter.ReadCsvFile(inputFilePath, True)
    mAge    = []
    mWeight = []
    mHeight = []
    mBmi    = []
    fAge    = []
    fWeight = []
    fHeight = []
    fBmi    = []

    for data in inputData:
        if (data[5] == 'Male'):
            mAge.append(int(data[6]))
            mWeight.append(float(data[0]))
            mHeight.append(float(data[1]))
            mBmi.append(float(data[2]))
        else:
            fAge.append(int(data[6]))
            fWeight.append(float(data[0]))
            fHeight.append(float(data[1]))
            fBmi.append(float(data[2]))
        
    
    #--- rcParams設定 ---#
    plt.rcParams['axes.axisbelow']  = True   # grid線を後ろに
    plt.rcParams['xtick.direction'] = 'out'
    plt.rcParams['ytick.direction'] = 'out'
    plt.rcParams['font.family']     = 'Meiryo'

    #--- オブジェクト生成 ---#
    # inch -> cm 変換式
    cm = 1 / 2.54
    fig, ax = plt.subplots(figsize=(12*cm, 10*cm))
    
    #--- グラフの描画設定 ---#
    ax.hist(
                mWeight,
                bins=40,
                #edgecolor='black',
                label='mWeight',
                )
    
    #--- 書式設定・出力設定 ---#
    # 目盛線, 補助線
    ax.grid(which = 'major', linestyle = 'dashed')      # grid線表示設定
    #ax.grid(which = 'minor', linestyle = 'dotted')     # grid線表示設定
    #plt.minorticks_on()                                # 補助目盛線表示

    # 各種名称設定
    #ax.set_title("Weight")                 # グラフタイトル名称
    ax.set_xlabel("Weight[kg]")             # X軸ラベル名称
    ax.set_ylabel("Number of People")       # Y軸ラベル名称

    # 軸メモリ設定
    xMin = 50
    xMax = 110
    yMin = 0
    yMax = 100
    xTicksOffset = 10
    yTicksOffset = 20

    ax.set_xticks(np.arange(xMin, xMax + 1, xTicksOffset))  # X軸メモリ刻み
    ax.set_yticks(np.arange(yMin, yMax + 1, yTicksOffset))  # Y軸メモリ刻み
    ax.set_xlim(xMin, xMax)                                 # X軸表示範囲
    ax.set_ylim(yMin, yMax)                                 # Y軸表示範囲
    
    # 凡例設定
    ax.legend(
                #fontsize='small',
                #markerscale=2, 
                ncol=1, 
                #columnspacing=0.2, 
                #handletextpad=0, 
                frameon=False, 
                shadow=False, 
                loc='upper center', 
                bbox_to_anchor=(0.5, -0.125)
                )
    
    # レイアウトを調整
    fig.tight_layout()

    # グラフ出力
    plt.savefig("./HistogramPlot.pdf", bbox_inches="tight", pad_inches=0.005)
    plt.show()

if __name__ == "__main__":
    main()
