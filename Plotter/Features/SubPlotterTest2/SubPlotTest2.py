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

#--- 関数宣言 ---#


#--- main関数 ---#
def main():

    #--- 変数宣言 ---#
    inputFile = 'Log.csv'
    _, exeFileDir = FileManager.GetExecPath(__file__)
    inputFilePath = os.path.join(exeFileDir, inputFile)

    inputData = FileReadWriter.ReadCsvFile(inputFilePath, True)
    time    = []
    i_A     = []
    v       = []

    for data in inputData[0]:
        time.append(float(data[6]))
        i_A.append(float(data[3]))
        v.append(float(data[4]))
        
    
    #--- rcParams設定 ---#
    plt.rcParams['axes.axisbelow']  = True   # grid線を後ろに
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.rcParams['font.family']     = 'Meiryo'

    #--- オブジェクト生成 ---#
    # inch -> cm 変換式
    cm = 1/2.54
    fig = plt.figure(figsize=(14*cm, 14*cm))

    #--- グラフの描画設定 ---#
    # 最初のグラフ
    ax1 = fig.add_subplot(2, 2, 1)
    ax1.plot(
                time,               # x軸値
                i_A,                # y軸値
                color="tab:orange", # 色
                linewidth=3,        # 線の太さ
                label = "Current"   # ラベル
                )
    
    # 2つ目のグラフ
    ax2 = fig.add_subplot(2, 2, 2)
    ax2.plot(
                time,               # x軸値
                v,                  # y軸値
                color="tab:blue",   # 色
                linewidth=3,        # 線の太さ
                label = "Voltage"   # ラベル
                )

    # 3つ目のグラフ
    ax3 = fig.add_subplot(2, 2, (3, 4))
    ax3.plot(
                time,               # x軸値
                i_A,                # y軸値
                color="tab:orange", # 色
                linewidth=3,        # 線の太さ
                label = "Current"   # ラベル
                )

    ax3.plot(
                time,               # x軸値
                v,                  # y軸値
                color="tab:blue",   # 色
                linewidth=3,        # 線の太さ
                label = "Voltage"   # ラベル
                )
    

    #--- 書式設定・出力設定 ---#
    # 目盛線, 補助線
    # 最初のグラフ
    ax1.grid(which = 'major', linestyle = 'dashed')   # grid線表示設定
    #ax.grid(which = 'minor', linestyle = 'dotted')     # grid線表示設定
    #plt.minorticks_on()                                # 補助目盛線表示

    # 2つ目のグラフ
    ax2.grid(which = 'major', linestyle = 'dashed')   # grid線表示設定
    #ax.grid(which = 'minor', linestyle = 'dotted')     # grid線表示設定
    #plt.minorticks_on()                                # 補助目盛線表示

    # 3つ目のグラフ
    ax3.grid(which = 'major', linestyle = 'dashed')   # grid線表示設定
    #ax.grid(which = 'minor', linestyle = 'dotted')     # grid線表示設定
    #plt.minorticks_on()                                # 補助目盛線表示


    # 各種名称設定
    #ax.set_title("Power")                  # グラフタイトル名称

    # 最初のグラフ
    ax1.set_xlabel("Time[sec]")  # X軸ラベル名称
    ax1.set_ylabel("Current[A]") # Y軸ラベル名称

    # 2つ目のグラフ
    ax2.set_xlabel("Time[sec]")  # X軸ラベル名称
    ax2.set_ylabel("Voltage[V]") # Y軸ラベル名称

    # 3つ目のグラフ
    ax3.set_xlabel("Time[sec]")  # X軸ラベル名称
    ax3.set_ylabel("Current[A],Voltage[V]") # Y軸ラベル名称

    # 軸メモリ設定
    xMin = 0
    xMax = 20
    yMin = 0
    yMax = 14
    xTicksOffset = 2
    yTicksOffset = 2

    # 最初のグラフ
    ax1.set_xticks(np.arange(xMin, xMax + 1, xTicksOffset))  # X軸メモリ刻み
    ax1.set_yticks(np.arange(yMin, yMax + 1, yTicksOffset))  # Y軸メモリ刻み
    ax1.set_xlim(xMin, xMax)                                 # X軸表示範囲
    ax1.set_ylim(yMin, yMax)                                 # Y軸表示範囲

    # 2つ目のグラフ
    ax2.set_xticks(np.arange(xMin, xMax + 1, xTicksOffset))  # X軸メモリ刻み
    ax2.set_yticks(np.arange(yMin, yMax + 1, yTicksOffset))  # Y軸メモリ刻み
    ax2.set_xlim(xMin, xMax)                                 # X軸表示範囲
    ax2.set_ylim(yMin, yMax)                                 # Y軸表示範囲

    # 3つ目のグラフ
    ax3.set_xticks(np.arange(xMin, xMax + 1, xTicksOffset))  # X軸メモリ刻み
    ax3.set_yticks(np.arange(yMin, yMax + 1, yTicksOffset))  # Y軸メモリ刻み
    ax3.set_xlim(xMin, xMax)                                 # X軸表示範囲
    ax3.set_ylim(yMin, yMax)                                 # Y軸表示範囲
    
    # 凡例設定
    # 最初のグラフ
    ax1.legend(
                #fontsize='small',
                markerscale=2, 
                ncol=1, 
                #columnspacing=0.2, 
                #handletextpad=0, 
                frameon=False, 
                shadow=False, 
                loc='lower center', 
                bbox_to_anchor=(0.5, 1.0)
                )

    # 2つ目のグラフ
    ax2.legend(
                #fontsize='small',
                markerscale=2, 
                ncol=1, 
                #columnspacing=0.2, 
                #handletextpad=0, 
                frameon=False, 
                shadow=False, 
                loc='lower center', 
                bbox_to_anchor=(0.5, 1.0)
                )

    # 3つ目のグラフ
    ax3.legend(
                #fontsize='small',
                markerscale=2, 
                ncol=2, 
                #columnspacing=0.2, 
                #handletextpad=0, 
                frameon=False, 
                shadow=False, 
                loc='lower center', 
                bbox_to_anchor=(0.5, 1.0)
                )
    
    # レイアウトを調整
    fig.tight_layout()

    # グラフ出力
    outputPath = os.path.join(exeFileDir, "SubPlotTest2.pdf")
    plt.savefig(outputPath, bbox_inches="tight")
    plt.show()

if __name__ == "__main__":
    main()
