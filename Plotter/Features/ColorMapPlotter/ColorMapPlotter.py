#!/usr/local/bin/python3
# coding: utf-8

###
# /* ColorMapPlotter.py */
# 
# 
###

#--- モジュールのインポート ---#
import sys
import os
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1 import make_axes_locatable

# プロジェクトのルートディレクトリをsys.pathに追加
#sys.path.append(os.path.join(os.path.dirname(__file__), '../../../'))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

#--- 自作モジュールのインポート ---#
from Utility import FileReadWriter, ExcelFileFormatter, FileManager, DataManager

#--- 変数宣言 ---#
curScript = sys.argv[0]

#--- main関数 ---#
def main():

    #--- rcParams設定 ---#
    plt.rcParams['axes.axisbelow']  = True   # grid線を後ろに
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.rcParams['font.family']     = 'Meiryo'

    #--- 2次関数のカラーマッププロット ---#
    xMin = -10
    xMax = 10
    yMin = -10
    yMax = 10

    # グリッドの作成
    x = np.linspace(xMin, xMax, 400)
    y = np.linspace(yMin, yMax, 400)
    X, Y = np.meshgrid(x, y)

    # 2次関数の定義
    Z = X**2 + Y**2

    # オブジェクト生成 (inch -> cm 変換)
    cm = 1 / 2.54
    fig, ax = plt.subplots(figsize=(10*cm, 10*cm))

    # 2次関数のカラーマップ表示
    c = ax.imshow(Z, extent=[xMin, xMax, yMin, yMax], origin='lower', cmap='turbo')

    # カラーバーの追加 (AxesDividerを使用して調整)
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.1)  # カラーバーの位置とサイズを調整
    cbar = fig.colorbar(c, cax=cax, label='Z value')

    # カラーバーの目盛りをカスタマイズ
    ticks = np.linspace(Z.min(), Z.max(), num=9)
    cbar.set_ticks(ticks)

    #--- 書式設定・出力設定 ---#
    # 各種名称設定
    ax.set_xlabel("X軸")
    ax.set_ylabel("Y軸")
    ax.set_title(r'$z = x^2 + y^2$')

    # 軸メモリ設定
    xTicksOffset = 2
    yTicksOffset = 2

    ax.set_xticks(np.arange(xMin, xMax + 1, xTicksOffset))  # X軸メモリ刻み
    ax.set_yticks(np.arange(yMin, yMax + 1, yTicksOffset))  # Y軸メモリ刻み
    ax.set_xlim(xMin, xMax)                                 # X軸表示範囲
    ax.set_ylim(yMin, yMax)                                 # Y軸表示範囲

    # レイアウトを調整
    fig.tight_layout()

    # グラフ出力
    plt.savefig("./ColorMapPlotter.pdf", bbox_inches="tight", pad_inches=0.05)
    plt.show()

if __name__ == "__main__":
    main()