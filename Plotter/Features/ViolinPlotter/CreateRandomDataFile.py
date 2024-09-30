#!/usr/local/bin/python3
# coding: utf-8

###
# /* CreateRandomDataFile.py */
# 
# 
###

#--- モジュールのインポート ---#
import sys
import os
import pandas as pd

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
    outputFile = 'RandomFile.csv'
    _, exeFileDir = FileManager.GetExecPath(__file__)
    inputFilePath = os.path.join(exeFileDir, inputFile)
    outputFilePath = os.path.join(exeFileDir, outputFile)

    # CSVファイルを読み込む（ヘッダー込み）
    data = pd.read_csv(inputFilePath)

    # ランダムに1000行を抽出（ヘッダーはそのまま）
    sampled_data = data.sample(n=200, random_state=42)

    # 抽出したデータを新しいCSVファイルに保存（ヘッダー付き）
    sampled_data.to_csv(outputFilePath, index=False)

if __name__ == "__main__":
    main()
