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

    inputFile = 'final_dataset_BFP.csv'
    exeFilePath = FileManager.GetExecFilePath(__file__)
    exeFileDir = os.path.dirname(exeFilePath)
    inputFilePath = os.path.join(exeFileDir, inputFile)

    inputData = FileReadWriter.ReadCsvFile(inputFilePath, True)
    mAge = []
    mWeight = []
    mHeight = []
    mBmi = []
    fAge = []
    fWeight = []
    fHeight = []
    fBmi = []

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
        

    #--- 変数宣言 ---#
    xMin = 15
    xMax = 61
    yMin = 15
    yMax = 41
    """
    xTicksOffset = 0.001
    yTicksOffset = 0.001
    """
    cm = 1 / 2.54       # inch -> cm 変換式

    #--- rcParams設定 ---#
    plt.rcParams['axes.axisbelow'] = True # grid線を後ろに
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.rcParams['font.family'] = 'Meiryo'
    #plt.rcParams['figure.figsize'] = (12*cm, 10*cm)    # グラフの大きさ


    fig, ax = plt.subplots(figsize=(12*cm, 10*cm))
    
    #--- グラフの描画設定 ---#
    ax.scatter(
                mWeight,                  # x軸値
                mHeight,                  # y軸値
                s=10,
                marker = "o",       # マーカーの形状
                label = "Male"      # ラベル
                )
    
    ax.scatter(
                fWeight,                  # x軸値
                fHeight,                  # y軸値
                s=10,
                marker = "*",       # マーカーの形状
                label = "Female"      # ラベル
                )
    
    #--- 書式設定・出力設定 ---#
    #plt.minorticks_on()                                             # 補助目盛線表示
    ax.grid(which = 'major', linestyle = 'dashed')                  # grid線表示設定
    #ax.grid(which = 'minor', linestyle = 'dotted')                  # grid線表示設定


    ax.set_title("Weight vs Height")    # グラフタイトル名称
    ax.set_xlabel("Weight")             # X軸ラベル名称
    ax.set_ylabel("Height")             # Y軸ラベル名称


    ax.set_xticks(np.arange(50, 116, 5))                # X軸メモリ間隔
    ax.set_yticks(np.arange(1.35, 2.06, 0.05))              # Y軸メモリ間隔
    ax.set_xlim(50, 110)
    ax.set_ylim(1.35, 2.00)

    ax.legend()          # 凡例

    #plt.savefig("./Matplotlib/sample.png")          # グラフの出力
    #plt.savefig("./sample.pdf")          # グラフの出力
    plt.savefig("./sample.pdf", bbox_inches="tight")          # グラフの出力
    plt.show()

if __name__ == "__main__":
    main()
