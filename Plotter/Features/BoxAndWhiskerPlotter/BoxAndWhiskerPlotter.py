#!/usr/local/bin/python3
# coding: utf-8

###
# /* BoxAndWhiskerPlotter.py */
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
    inputFile = 'RandomFile.csv'
    _, exeFileDir = FileManager.GetExecPath(__file__)
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
    dummy   = []

    for data in inputData[0]:
        if (data[5] == 'Male'):
            mAge.append(int(data[6]))
            mWeight.append(float(data[0]))

            mHeight.append(float(data[1]))
            mBmi.append(float(data[2]))

            # 今回だけ特別にdummyを詰める
            dummy.append(float(data[0]))

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
    
    #--- バイオリンプロットの描画設定 ---#
    data = [mWeight, fWeight, dummy]

    # 各バイオリンの位置を設定
    increment = 0.7  # バイオリン間の距離
    positions = [1]  # 初期位置を1に設定
    for i in range(1, len(data)):
        positions.append(positions[i-1] + increment)  # 前のポジションに倍率をかけて次の位置を決める

    # 箱ひげ図の描画
    ax.boxplot(data, positions=positions, showmeans=True, meanline=True, patch_artist=False)  # patch_artistをFalseに設定

    #--- 書式設定・出力設定 ---#
    # 目盛線, 補助線
    ax.grid(which = 'major', axis='y', linestyle = 'dashed')    # grid線表示設定

    # 各種名称設定
    ax.set_title("Weight Distribution by Gender")   # グラフタイトル名称
    ax.set_xlabel("Gender")                         # X軸ラベル名称
    ax.set_ylabel("Weight")                         # Y軸ラベル名称

    # 軸メモリ設定
    yMin = 0
    yMax = 180
    yTicksOffset = 20

    ax.set_xticks(positions)                                    # X軸ラベルの位置
    ax.set_xticklabels(["Male", "Female", "Dummy"])             # X軸ラベル名称
    ax.set_yticks(np.arange(yMin, yMax + 0.01, yTicksOffset))   # Y軸メモリ刻み
    ax.set_ylim(yMin, yMax)                                     # Y軸範囲設定
    
    # レイアウトを調整
    fig.tight_layout()

    # グラフ出力
    outputPath = os.path.join(exeFileDir, "BoxAndWhiskerPlotter.pdf")
    plt.savefig(outputPath, bbox_inches="tight", pad_inches=0.05)
    plt.show()

if __name__ == "__main__":
    main()
