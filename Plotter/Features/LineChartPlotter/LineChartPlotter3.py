#!/usr/local/bin/python3
# coding: utf-8

###
# /* LineChartPlotter3.py */
# 
# 
###

#--- モジュールのインポート ---#
import sys
import os
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

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
    inputFile = 'Data.xlsx'
    _, exeFileDir = FileManager.GetExecPath(__file__)
    inputFilePath = os.path.join(exeFileDir, inputFile)

    inputData = FileReadWriter.ReadExcel(inputFilePath, headerSkip=True)
    date        = []
    weight      = []
    bFatPer     = []

    for data in inputData[0]:

        if  data[1] != None:
            # 日付データの変換
            raw_date = data[0]  # 例: "2025-01-03 00:00:00"
            #formatted_date = raw_date.strftime("%y-%m-%d")
            formatted_date = raw_date.strftime("%m-%d")
            date.append(formatted_date)  # フォーマット済みの日付を追加

            weight.append(float(data[1]))
            bFatPer.append(float(data[2]))
    
    #--- rcParams設定 ---#
    plt.rcParams['axes.axisbelow']  = True   # grid線を後ろに
    plt.rcParams['xtick.direction'] = 'out'
    plt.rcParams['ytick.direction'] = 'out'
    plt.rcParams['font.family']     = 'Meiryo'

    #--- オブジェクト生成 ---#
    # inch -> cm 変換式
    cm = 1 / 2.54
    fig, ax = plt.subplots(figsize=(18*cm, 10*cm))
    
    #--- グラフの描画設定 ---#
    ax.plot(
            date,               # x軸値
            weight,             # y軸値
            marker='o',         # 点の種類
            markersize='5',     # 点の大きさ
            linestyle='--',     # 線の種類
            linewidth=1,        # 線の太さ
            label = "Data[unit]"   # ラベル
            )
    
    # 各データポイントに値を表示
    for i in range(len(date)):
        ax.text(
            date[i], weight[i] + 0.2, f'{weight[i]:.1f}', fontsize=7, color='black',
            ha='center', va='bottom'  # 中央揃えで少し上に表示
        )
    
    # 背景色を区間ごとに変更
    ax.axhspan(0, 66, facecolor="tab:green", alpha=0.15)

    #--- 書式設定・出力設定 ---#
    # 目盛線, 補助線
    ax.grid(which = 'major', linestyle = 'dashed')      # grid線表示設定
    #plt.minorticks_on()                                # 補助目盛線表示
    #ax.grid(which = 'minor', linestyle = 'dotted')     # grid線表示設定

    # 各種名称設定
    ax.set_title("Dataの推移", fontweight='bold') # グラフタイトル名称
    ax.set_xlabel("月日")                               # X軸ラベル名称
    ax.set_xticks(range(len(date)))                     # 目盛り位置を設定
    ax.set_xticklabels(date, rotation=90)               # X軸ラベル回転
    ax.set_ylabel("Data[unit]")                           # Y軸ラベル名称

    # 軸メモリ設定
    yMin = 64
    yMax = 80
    yTicksOffset = 1

    ax.set_yticks(np.arange(yMin, yMax + 1, yTicksOffset))  # Y軸メモリ刻み
    ax.set_ylim(yMin, yMax)                                 # Y軸表示範囲
    
    # 凡例設定
    ax.legend(
                #fontsize='small',
                markerscale=1, 
                ncol=2, 
                #columnspacing=0.2, 
                #handletextpad=0, 
                frameon=False, 
                shadow=False, 
                loc='upper center', 
                bbox_to_anchor=(0.5, -0.26)
                )
    
    # X軸方向の余白を減らすための調整
    ax.margins(x=0.02)  # X方向の余白を減らす

    # レイアウトを調整
    fig.tight_layout()

    # グラフ出力
    outputPath = os.path.join(exeFileDir, "LineChartPlotter3.pdf")
    plt.savefig(outputPath, bbox_inches="tight", pad_inches=0.05)
    plt.show()

if __name__ == "__main__":
    main()
