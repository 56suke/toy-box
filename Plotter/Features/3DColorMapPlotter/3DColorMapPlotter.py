#!/usr/local/bin/python3
# coding: utf-8

###
# /* 3DColorMapPlotter.py */
# 
# 
###

#--- モジュールのインポート ---#
import sys
import os
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

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
    zMin = 0
    zMax = 200

    # グリッドの作成
    x = np.linspace(xMin, xMax, 400)
    y = np.linspace(yMin, yMax, 400)
    X, Y = np.meshgrid(x, y)

    # 数式の定義 (文字列として数式を定義)
    equation = "X**2 + Y**2"  # 任意の式をここで指定
    Z = eval(equation, {"X": X, "Y": Y})  # evalで式を評価し、Zを計算
    
    # LaTeXで使える形に変換: **2 を ^2 に置き換える
    equation_latex = equation.replace("**2", "^2")

    # オブジェクト生成 (inch -> cm 変換), 3Dプロットのためのprojection指定をsubplotsで行う
    cm = 1 / 2.54
    fig, ax = plt.subplots(figsize=(12*cm, 12*cm), subplot_kw={"projection": "3d"})

    # 3Dサーフェスプロットの作成
    surface = ax.plot_surface(X, Y, Z, cmap='turbo', edgecolor='none', vmin=zMin, vmax=zMax)

    # カラーバーの追加 (サイズとパディングを調整)
    levels = np.arange(0, 200 + 1, 20)
    cbar = fig.colorbar(surface, ax=ax, shrink=0.5, aspect=15, pad=0.15, label='Z value')
    # カラーバーの目盛りを設定
    cbar.set_ticks(levels)
    # カラーバーの目盛りを外向きに設定
    cbar.ax.tick_params(direction='out')

    #--- 書式設定・出力設定 ---#
    # 各種名称設定
    ax.set_xlabel("X軸")
    ax.set_ylabel("Y軸")
    ax.set_zlabel("Z軸", rotation=90)
    # タイトルに数式を反映
    ax.set_title(rf'$z = {equation_latex}$')  # LaTeX形式で数式を表示

    # 軸メモリ設定
    xTicksOffset = 2
    yTicksOffset = 2
    zTicksOffset = 20

    ax.set_xticks(np.arange(xMin, xMax + 1, xTicksOffset))  # X軸メモリ刻み
    ax.set_yticks(np.arange(yMin, yMax + 1, yTicksOffset))  # Y軸メモリ刻み
    ax.set_zticks(np.arange(zMin, zMax + 1, zTicksOffset))  # Z軸メモリ刻み

    ax.set_xlim(xMin, xMax)                                 # X軸表示範囲
    ax.set_ylim(yMin, yMax)                                 # Y軸表示範囲
    ax.set_zlim(zMin, zMax)                                 # Z軸表示範囲

    # レイアウトを調整
    fig.tight_layout()

    # グラフ出力
    _, dirPath = FileManager.GetExecPath(__file__)
    outputPath = os.path.join(dirPath, "3DColorMapPlotter.pdf")
    plt.savefig(outputPath, bbox_inches="tight", pad_inches=0.05)
    plt.show()

if __name__ == "__main__":
    main()