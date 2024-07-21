#!/usr/local/bin/python3
# coding: utf-8

###
# /* PlotTest.py */
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
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.rcParams['font.family']     = 'Meiryo'

    #--- オブジェクト生成 ---#
    # inch -> cm 変換式
    cm = 1 / 2.54
    fig, ax = plt.subplots(figsize=(12*cm, 10*cm))
    
    #--- グラフの描画設定 ---#
    ax.scatter(
                mWeight,            # x軸値
                mHeight,            # y軸値
                marker = "o",       # マーカーの形状
                s = 10,             # マーカーサイズ
                alpha = 0.7,        # マーカーの透明度
                label = "Male"      # ラベル
                )
    
    ax.scatter(
                fWeight,            # x軸値
                fHeight,            # y軸値
                marker = "*",       # マーカーの形状
                s = 10,             # マーカーサイズ
                alpha = 0.7,        # マーカーの透明度
                label = "Female"    # ラベル
                )
    
    #--- 書式設定・出力設定 ---#
    # 目盛線, 補助線
    ax.grid(which = 'major', linestyle = 'dashed')      # grid線表示設定
    #plt.minorticks_on()                                # 補助目盛線表示
    #ax.grid(which = 'minor', linestyle = 'dotted')     # grid線表示設定

    # 各種名称設定
    ax.set_title("Weight vs Height")    # グラフタイトル名称
    ax.set_xlabel("Weight")             # X軸ラベル名称
    ax.set_ylabel("Height")             # Y軸ラベル名称

    # 軸メモリ設定
    xMin = 50
    xMax = 110
    yMin = 1.35
    yMax = 2.00
    xTicksOffset = 5
    yTicksOffset = 0.05

    ax.set_xticks(np.arange(xMin, xMax + 1, xTicksOffset))      # X軸メモリ刻み
    ax.set_yticks(np.arange(yMin, yMax + 0.01, yTicksOffset))   # Y軸メモリ刻み
    ax.set_xlim(xMin, xMax)                                     # X軸表示範囲
    ax.set_ylim(yMin, yMax)                                     # Y軸表示範囲
    
    # 凡例設定
    ax.legend(
                #fontsize='small',
                markerscale=2, 
                ncol=2, 
                columnspacing=0.2, 
                handletextpad=-0.2, 
                frameon=False, 
                shadow=False, 
                loc='upper center', 
                bbox_to_anchor=(0.5, -0.1)
                )
    
    # レイアウトを調整
    fig.tight_layout()

    # グラフ出力
    plt.savefig("./ScatterPlotSample.pdf", bbox_inches="tight")
    plt.show()

if __name__ == "__main__":
    main()
