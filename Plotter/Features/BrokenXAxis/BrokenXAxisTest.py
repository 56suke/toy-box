#!/usr/local/bin/python3
# coding: utf-8

###
# /* BrokenAxisTest.py */
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

    #--- rcParams設定 ---#
    plt.rcParams['axes.axisbelow']  = True  # grid線を後ろに
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.rcParams['font.family']     = 'Meiryo'

    #--- オブジェクト生成 ---#
    # inch -> cm 変換式
    cm = 1 / 2.54
    fig, (ax1, ax2) = plt.subplots(1, 2, sharex=False, sharey=True, figsize=(12*cm, 8*cm), gridspec_kw={'width_ratios': [5, 3]})

    # 左のプロット (低いX軸範囲)
    ax1.plot(time, i_A, color="tab:orange", linewidth=3, label="Current")
    ax1.grid(which='major', linestyle='dashed')
    ax1.spines['right'].set_visible(False)

    # 右のプロット (高いX軸範囲)
    ax2.plot(time, i_A, color="tab:orange", linewidth=3, label="Current")
    ax2.grid(which='major', linestyle='dashed')
    ax2.spines['left'].set_visible(False)
    ax2.tick_params(labelleft=False, left=False)

    # 各種名称設定
    # X軸ラベルはfig.textを使って設定
    fig.text(0.5, 0, 'Time[sec]', ha='center')
    ax1.set_ylabel("Current[A]")  # Y軸ラベル名称

    # 軸メモリ設定
    xMin = 0
    xMax = 18
    yMin = 0
    yMax = 12
    xTicksOffset = 2
    yTicksOffset = 2

    ax1.set_xticks(np.arange(xMin, xMax + 1, xTicksOffset)) # X軸メモリ刻み
    ax1.set_yticks(np.arange(yMin, yMax + 1, yTicksOffset)) # Y軸メモリ刻み
    ax1.set_xlim(0, 10)                                     # X軸表示範囲
    ax1.set_ylim(yMin, yMax)                                # Y軸表示範囲

    ax2.set_xticks(np.arange(xMin, xMax + 1, xTicksOffset)) # X軸メモリ刻み
    ax2.set_yticks(np.arange(yMin, yMax + 1, yTicksOffset)) # Y軸メモリ刻み
    ax2.set_xlim(12, 18)                                    # X軸表示範囲
    ax2.set_ylim(yMin, yMax)                                # Y軸表示範囲
    
    # 凡例設定
    handles, labels = ax1.get_legend_handles_labels()
    fig.legend(
                handles,
                labels,
                #fontsize='small',
                markerscale=2, 
                ncol=1, 
                #columnspacing=0.2, 
                #handletextpad=0, 
                frameon=False, 
                shadow=False, 
                #loc='lower center', 
                #bbox_to_anchor=(0.5, 1.0),
                loc='upper center', 
                bbox_to_anchor=(0.5, 0)
                )

    # ギャップを示すためのデコレーション（斜め線）
    d = .5  # proportion of vertical to horizontal extent of the slanted line
    kwargs = dict(marker=[(-d, -1), (d, 1)], markersize=6,
              linestyle="none", color='k', mec='k', mew=1, clip_on=False)
    ax1.plot([1, 1], [0, 1], transform=ax1.transAxes, **kwargs)
    ax2.plot([0, 0], [0, 1], transform=ax2.transAxes, **kwargs)

    # レイアウトを調整
    fig.tight_layout()
    fig.subplots_adjust(wspace=0.1)  # hspaceを小さくして間隔を狭める

    # グラフ出力
    plt.savefig("./BrokenXAxisTest.pdf", bbox_inches="tight", pad_inches=0.005)
    plt.show()

if __name__ == "__main__":
    main()
