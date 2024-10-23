#!/usr/local/bin/python3
# coding: utf-8

###
# /* GanttChartPlotter2.py */
# 
# 
###

#--- モジュールのインポート ---#
import sys
import os
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches 

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
    inputFile = 'SampleGanttTaskData.csv'
    _, exeFileDir = FileManager.GetExecPath(__file__)
    inputFilePath = os.path.join(exeFileDir, inputFile)

    inputData   = FileReadWriter.ReadCsvFile(inputFilePath, True)
    date        = []
    time        = []
    eventName   = []
    elapsedTime = []
    diffTime    = []
    startTime   = []
    eventType   = []

    # 最初のイベントの時刻を基準にするための変数
    baseTime = None

    for data in inputData[0]:
        date.append(data[0])
        time.append(data[1])
        eventName.append(data[2])
        elapsedTime.append(float(data[3]))
        eventType.append(data[5])

        dTime = float(data[4])
        diffTime.append(dTime)

        # 時刻から経過時間を計算
        if baseTime is None:
            baseTime = dTime # 最初のイベントの時間を基準とする
        startTime.append(dTime - baseTime)
    
    #--- rcParams設定 ---#
    plt.rcParams['axes.axisbelow']  = True   # grid線を後ろに
    plt.rcParams['xtick.direction'] = 'out'
    plt.rcParams['ytick.direction'] = 'out'
    plt.rcParams['font.family']     = 'Meiryo'

    #--- オブジェクト生成 ---#
    # inch -> cm 変換式
    cm = 1 / 2.54
    fig, ax = plt.subplots(figsize=(18*cm, 14*cm))

    # 色と凡例用の定義
    color_map = {'A': 'tab:red', 'B': 'tab:blue', 'C': 'tab:olive', 'D': 'tab:green'}
    legend_patches = []

    # 各イベントのバーを描画
    for i in range(len(eventName)):
        color = color_map.get(eventType[i], 'tab:green')  # デフォルト色は 'tab:green'

        ax.barh(eventName[i], elapsedTime[i], left=startTime[i], color=color)

        # 各棒の横に値を表示
        sTime = startTime[i]
        eTime = elapsedTime[i]
        ax.text(sTime + eTime + 0.2, i, f'{eTime:.2f} [sec]', va='center')

    #--- 凡例の作成 ---#
    # 一度だけパッチを作成するためのコード
    for event_type, color in color_map.items():
        legend_patches.append(mpatches.Patch(color=color, label=f'EventType:{event_type}'))

    # 凡例設定
    ax.legend(
                handles=legend_patches,
                ncol=4,
                frameon=False, 
                shadow=False, 
                loc='upper center', 
                bbox_to_anchor=(0.5, -0.1)
                )

    #--- 書式設定・出力設定 ---#
    # 目盛線, 補助線
    ax.grid(which = 'major', linestyle = 'dashed')  # grid線表示設定

    # 各種名称設定
    ax.set_xlabel("Elapsed Time [sec]") # X軸ラベル名称
    ax.set_ylabel("Event Name")              # Y軸ラベル名称

    # 軸メモリ設定
    xMin = 0
    xMax = 50
    xTicksOffset = 2
    ax.set_xticks(np.arange(xMin, xMax + 1, xTicksOffset))  # X軸メモリ刻み
    ax.set_xlim(xMin, xMax)                                 # X軸表示範囲

    # Y軸方向の余白を減らすための調整
    ax.margins(y=0.02)  # Y方向の余白を減らす

    # y軸の順序を反転
    ax.invert_yaxis()

    # レイアウトを調整
    fig.tight_layout()

    # グラフ出力
    outputPath = os.path.join(exeFileDir, "GanttChartPlotter2.pdf")
    plt.savefig(outputPath, bbox_inches="tight", pad_inches=0.05)
    plt.show()

if __name__ == "__main__":
    main()