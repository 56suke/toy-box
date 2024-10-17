#!/usr/local/bin/python3
# coding: utf-8

###
# /* JointScatterHistogramPlotter.py */
# 
# 
###

#--- モジュールのインポート ---#
import sys
import os
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec

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

    for data in inputData[0]:
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
    fig = plt.figure(figsize=(14*cm, 14*cm), constrained_layout=True)
    gs = GridSpec(4, 4, figure=fig)

    ax_main = fig.add_subplot(gs[1:4, 0:3])
    ax_hist_x = fig.add_subplot(gs[0, 0:3], sharex=ax_main)
    ax_hist_y = fig.add_subplot(gs[1:4, 3], sharey=ax_main)
    
    #--- 散布図の描画設定 ---#
    ax_main.scatter(
        fWeight,            # x軸値
        fHeight,            # y軸値
        marker = "*",       # マーカーの形状
        color='tab:blue',   # マーカーの色
        s = 10,             # マーカーサイズ
        alpha = 0.7,        # マーカーの透明度
        label = "Female"    # ラベル
    )
    
    #--- ヒストグラム描画 ---#
    ax_hist_x.hist(fWeight, bins=20, alpha=0.7, color='tab:blue')
    ax_hist_y.hist(fHeight, bins=20, orientation='horizontal', alpha=0.7, color='tab:blue')
    
    # 軸のラベルを隠す（不要なラベルを表示しないようにする）
    plt.setp(ax_hist_x.get_xticklabels(), visible=False)
    plt.setp(ax_hist_y.get_yticklabels(), visible=False)
    
    #--- 書式設定・出力設定 ---#
    # grid線表示設定
    ax_main.grid(which = 'major', linestyle = 'dashed')
    ax_hist_x.grid(which='major', linestyle='dashed')
    ax_hist_y.grid(which='major', linestyle='dashed')

    ax_main.set_xlabel("Weight")            # 散布図X軸ラベル名称
    ax_main.set_ylabel("Height")            # 散布図Y軸ラベル名称
    ax_hist_y.set_xlabel('Frequency')       # ヒストグラムX軸ラベル名称
    ax_hist_x.set_ylabel('Frequency')       # ヒストグラムY軸ラベル名称

    # 軸メモリ設定
    xMin = 50
    xMax = 110
    yMin = 1.35
    yMax = 1.85
    xTicksOffset = 5
    yTicksOffset = 0.05

    ax_main.set_xticks(np.arange(xMin, xMax + 1, xTicksOffset))      # X軸メモリ刻み
    ax_main.set_yticks(np.arange(yMin, yMax + 0.01, yTicksOffset))   # Y軸メモリ刻み
    ax_main.set_xlim(xMin, xMax)                                     # X軸表示範囲
    ax_main.set_ylim(yMin, yMax)                                     # Y軸表示範囲
    
    # 凡例設定
    ax_main.legend(
        #fontsize='small',
        markerscale=2, 
        ncol=1, 
        columnspacing=0.2, 
        handletextpad=-0.2, 
        frameon=False, 
        shadow=False, 
        loc='upper center', 
        bbox_to_anchor=(0.5, -0.1)
    )

    # グラフ出力
    outputPath = os.path.join(exeFileDir, "JointScatterHistogramPlotter.pdf")
    plt.savefig(outputPath, bbox_inches="tight", pad_inches=0.05)
    plt.show()

if __name__ == "__main__":
    main()
