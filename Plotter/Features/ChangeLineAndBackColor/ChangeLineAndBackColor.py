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
    inputFile = 'Log.csv'
    exeFilePath = FileManager.GetExecFilePath(__file__)
    exeFileDir = os.path.dirname(exeFilePath)
    inputFilePath = os.path.join(exeFileDir, inputFile)

    inputData = FileReadWriter.ReadCsvFile(inputFilePath, True)
    time    = []
    i_A     = []

    for data in inputData:
        time.append(float(data[6]))
        i_A.append(float(data[3]))
        
    # NumPy配列に変換
    time = np.array(time)
    i_A = np.array(i_A)
    
    #--- rcParams設定 ---#
    plt.rcParams['axes.axisbelow']  = True   # grid線を後ろに
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.rcParams['font.family']     = 'Meiryo'

    #--- オブジェクト生成 ---#
    # inch -> cm 変換式
    cm = 1/2.54
    fig, ax = plt.subplots(figsize=(12*cm, 8*cm))
    
    #--- グラフの描画設定 ---#
    # 最初のプロット
    ax.plot(
                time[time <= 8],    # x軸値
                i_A[time <= 8],     # y軸値
                color="tab:red",    # 色
                linewidth=3,        # 線の太さ
                #label = "Current"   # ラベル
                )

    # 2つ目のプロット
    ax.plot(
                time[(time > 8) & (time <= 16)],    # x軸値
                i_A[(time > 8) & (time <= 16)],     # y軸値
                color="tab:blue",                   # 色
                linewidth=3                         # 線の太さ
                #label = "Current"                  # ラベル
                )
    
    # 3つ目のプロット
    ax.plot(
                time[(time > 16)],  # x軸値
                i_A[(time > 16)],   # y軸値
                color="tab:green",  # 色
                linewidth=3         # 線の太さ
                #label = "Current"  # ラベル
                )
    
    # 背景色を区間ごとに変更
    ax.axvspan(0, 8, facecolor="tab:red", alpha=0.15)
    ax.axvspan(8, 16, facecolor="tab:blue", alpha=0.15)
    ax.axvspan(16, 20, facecolor="tab:green", alpha=0.15)

    #--- 書式設定・出力設定 ---#
    # 目盛線, 補助線
    ax.grid(which = 'major', linestyle = 'dashed')      # grid線表示設定
    #plt.minorticks_on()                                # 補助目盛線表示
    #ax.grid(which = 'minor', linestyle = 'dotted')     # grid線表示設定

    # 各種名称設定
    #ax.set_title("Power")                  # グラフタイトル名称
    ax.set_xlabel("Time[sec]")              # X軸ラベル名称
    ax.set_ylabel("Current[A]") # Y軸ラベル名称

    # 軸メモリ設定
    xMin = 0
    xMax = 18
    yMin = 0
    yMax = 14
    xTicksOffset = 2
    yTicksOffset = 2

    ax.set_xticks(np.arange(xMin, xMax + 1, xTicksOffset))  # X軸メモリ刻み
    ax.set_yticks(np.arange(yMin, yMax + 1, yTicksOffset))  # Y軸メモリ刻み
    ax.set_xlim(xMin, xMax)                                 # X軸表示範囲
    ax.set_ylim(yMin, yMax)                                 # Y軸表示範囲
    
    # 凡例設定
    """
    ax.legend(
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
    """
    
    
    # レイアウトを調整
    fig.tight_layout()

    # グラフ出力
    plt.savefig("./ChangeLineAndBackColor.pdf", bbox_inches="tight")
    plt.show()

if __name__ == "__main__":
    main()
