#!/usr/local/bin/python3
# coding: utf-8

###
# /* ViolinPlotter.py */
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

    for data in inputData:
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

    # バイオリンプロットの描画
    parts = ax.violinplot(data, positions=positions, showmeans=True, showextrema=True, showmedians=False)

    #--- 各バイオリンの色を設定 ---#
    colors = ['tab:blue', 'tab:orange', 'tab:green']
    for i, pc in enumerate(parts['bodies']):
        pc.set_facecolor(colors[i]) # 各バイオリンの塗りつぶし色を設定
        #pc.set_edgecolor('black')  # 外枠の色を黒に設定

    # 平均値の色を設定
    parts['cmeans'].set_color('C1')  # 平均値の線の色を設定

    #--- 四分位数・平均値を描画 ---#
    for i, dataset in enumerate(data):
        q1 = np.percentile(dataset, 25)  # 第1四分位数
        q2 = np.percentile(dataset, 50)  # 中央値
        q3 = np.percentile(dataset, 75)  # 第3四分位数
        mean = np.mean(dataset)  # 平均値

        # バイオリンプロットの頂点データ（x, y座標）を取得
        vertices = parts['bodies'][i].get_paths()[0].vertices
        x_data = vertices[:, 0]
        y_data = vertices[:, 1]

        # 特定の四分位数に対応するx座標の範囲を取得する関数
        def get_violin_width_at_quantile(quantile_value):
            idx = np.abs(y_data - quantile_value).argmin()  # 最も近いy値のインデックスを取得
            x_min = x_data[idx]  # 対応するxの最小値
            x_max = x_data[-(idx + 1)]  # 対応するxの最大値
            return x_min, x_max

        # 四分位数や平均値のx範囲を取得
        q1_xmin, q1_xmax = get_violin_width_at_quantile(q1)
        q2_xmin, q2_xmax = get_violin_width_at_quantile(q2)
        q3_xmin, q3_xmax = get_violin_width_at_quantile(q3)
        mean_xmin, mean_xmax = get_violin_width_at_quantile(mean)

        # 四分位数や平均値の線を描画
        ax.hlines(q1, xmin=q1_xmin, xmax=q1_xmax, colors='black', linestyles='dotted')  # 第1四分位数
        ax.hlines(q2, xmin=q2_xmin, xmax=q2_xmax, colors='black', linestyles='dashed')  # 中央値
        ax.hlines(q3, xmin=q3_xmin, xmax=q3_xmax, colors='black', linestyles='dotted')  # 第3四分位数
        ax.hlines(mean, xmin=mean_xmin, xmax=mean_xmax, colors='tab:orange', linestyles='solid')  # 平均値
    
    #--- 書式設定・出力設定 ---#
    # 目盛線, 補助線
    ax.grid(which = 'major', axis='y', linestyle = 'dashed')    # grid線表示設定

    # 各種名称設定
    ax.set_title("Weight Distribution by Gender")   # グラフタイトル名称
    ax.set_xlabel("Gender")                         # X軸ラベル名称
    ax.set_ylabel("Weight")                         # Y軸ラベル名称

    # 軸メモリ設定
    yMin = 40
    yMax = 120
    yTicksOffset = 10

    ax.set_xticks(positions)                                    # X軸ラベルの位置
    ax.set_xticklabels(["Male", "Female", "Dummy"])             # X軸ラベル名称
    ax.set_yticks(np.arange(yMin, yMax + 0.01, yTicksOffset))   # Y軸メモリ刻み
    ax.set_ylim(40, 120)                                        # Y軸範囲設定
    
    # レイアウトを調整
    fig.tight_layout()

    # グラフ出力
    outputPath = os.path.join(exeFileDir, "ViolinPlotter.pdf")
    plt.savefig(outputPath, bbox_inches="tight", pad_inches=0.05)
    plt.show()

if __name__ == "__main__":
    main()
