#!/usr/local/bin/python3
# coding: utf-8

###
# /* RadarChartPlotter.py */
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

#--- レーダーチャート描画用関数 ---#
def make_radar_chart(categories, scores, label, color, ax):
    # 角度を計算
    N = len(categories)
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
    scores += scores[:1]  # 最初の値を末尾に追加してループを完成
    angles += angles[:1]  # 同様に角度もループするように設定

    # カテゴリの開始位置を調整（ここでは最初のカテゴリを右側に配置）
    ax.set_theta_offset(np.pi / 2)  # 90度から描画するように設定（上側が0度）
    ax.set_theta_direction(-1)  # 時計回りに描画

    # データ描画
    ax.fill(angles, scores, color=color, alpha=0.25)
    ax.plot(angles, scores, color=color, linewidth=1, label=label)

    yMin        = 0
    yMax        = 100
    yTicks      = 10
    yTicksNum   = int(yMax / yTicks)

    # Y軸目盛りを0から100の範囲で10刻みで表示
    ax.set_rlabel_position(0)  # 目盛りラベルの位置を調整
    ax.set_yticks(np.arange(yMin, yMax + 1, yTicks))  # 0から100まで10刻みで目盛り設定
    ax.set_ylim(yMin, yMax)

    # Y軸のメモリラベルを設定
    yticklabels = [str(i) for i in range(yMin, yMax + 1, yTicks)]
    ax.set_yticklabels(yticklabels, fontsize=8)

    # カテゴリラベルを設定
    ax.set_xticks(angles[:-1])  # カテゴリラベルの位置を設定
    ax.set_xticklabels(categories)  # カテゴリラベルを設定

    #--- 円周を削除して多角形を描画 ---#
    ax.spines['polar'].set_visible(False)  # 円形の外枠を非表示にする
    ax.grid(False)  # 円形グリッド線を非表示にする

    #--- 多角形の外枠を描画 ---#
    for i in range(1, (yTicksNum + 1)):  # 多角形を描画
        if(i < yTicksNum):
            ax.plot(angles, [yMax / yTicksNum * i] * (N+1), color='gray', linewidth=0.75, linestyle='solid', zorder=0)
        else:
            ax.plot(angles, [yMax / yTicksNum * i] * (N+1), color='black', linewidth=1, linestyle='solid', zorder=0)


    #--- 放射状の直線を描画 ---#
    for angle in angles[:-1]:
        ax.plot([angle, angle], [yMin, yMax], color='gray', linewidth=0.75, linestyle='solid', zorder=0)

    return ax

#--- main関数 ---#
def main():

    #--- 変数宣言 ---#
    inputFile = 'testResult.csv'
    _, exeFileDir = FileManager.GetExecPath(__file__)
    inputFilePath = os.path.join(exeFileDir, inputFile)
    inputData = FileReadWriter.ReadCsvFile(inputFilePath, True)

    categories = ['国語', '数学', '英語', '理科', '社会']  # 各科目名
    aScore = []
    bScore = []

    for data in inputData[0]:
        if data[0] == 'A':
            aScore = list(map(int, data[1:]))  # Aさんのスコア
        elif data[0] == 'B':
            bScore = list(map(int, data[1:]))  # Bさんのスコア
        
    
    #--- rcParams設定 ---#
    plt.rcParams['axes.axisbelow']  = True   # grid線を後ろに
    plt.rcParams['font.family']     = 'Meiryo'

    #--- オブジェクト生成 ---#
    # inch -> cm 変換式
    cm = 1 / 2.54
    fig, ax = plt.subplots(figsize=(12*cm, 12*cm), subplot_kw={'polar': True})  # polar=Trueを追加

    #--- レーダーチャート描画 ---#
    make_radar_chart(categories, aScore, 'Aさん', 'red', ax)
    make_radar_chart(categories, bScore, 'Bさん', 'blue', ax)

    #--- 書式設定・出力設定 ---#
    # 目盛線, 補助線
    #ax.grid(which = 'major', linestyle = 'dashed')      # grid線表示設定
    #ax.grid(which = 'major', linestyle = 'solid')      # grid線表示設定

    # グラフタイトル設定
    plt.title("テスト結果比較")

    # 凡例設定
    legend = ax.legend(
                #fontsize='small',
                markerscale=2, 
                ncol=2, 
                columnspacing=1, 
                #handletextpad=0, 
                frameon=False, 
                shadow=False, 
                loc='upper center', 
                bbox_to_anchor=(0.5, 0.0)
            )
    
    # 凡例内の線の太さを変更
    for line in legend.get_lines():
        line.set_linewidth(3)  # 線の太さを2に設定

    # レイアウトを調整
    fig.tight_layout()

    # グラフ出力
    outputPath = os.path.join(exeFileDir, "RadarChartPlotter.pdf")
    plt.savefig(outputPath, bbox_inches="tight", pad_inches=0.1)
    plt.show()

if __name__ == "__main__":
    main()
