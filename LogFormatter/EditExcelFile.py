#!/usr/local/bin/python3
# coding: utf-8

###
# EidtExcelFile
# エクセルファイル編集スクリプト
# 
###

#--- モジュールのインポート ---#
import sys
import openpyxl

#--- 変数宣言 ---#
curScript = sys.argv[0]
ROW_HEIGHT_RATIO = 1.3


#--- セルの列幅の自動調整 ---#
# inputFile:入力'.xlsxファイル'(.xlsxまでのパス)
def AdjustColWidth(inputFile):
    #--- 変数宣言 ---#

    # Excelファイルを開く
    wb = openpyxl.load_workbook(inputFile)
    # アクティブなシートを取得する
    ws = wb.active

    # セルの幅を自動調整
    for column in ws.columns:
        max_length = 0
        column_letter = openpyxl.utils.get_column_letter(column[0].column)
        for cell in column:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(cell.value)
            except:
                pass
        adjusted_width = (max_length + 2) * 1.2 # 適切な調整値を加える
        ws.column_dimensions[column_letter].width = adjusted_width

    # Excelファイルを保存
    wb.save(inputFile)


#--- セルの行高設定(引数指定) ---#
# inputFile:入力'.xlsxファイル'(.xlsxまでのパス)
# hVal:セルの行高
def SetRowHeight(inputFile, hVal):
    #--- 変数宣言 ---#

    # Excelファイルを開く
    wb = openpyxl.load_workbook(inputFile)
    # アクティブなシートを取得する
    ws = wb.active

    # 行高を設定
    for row in ws.iter_rows():
        ws.row_dimensions[row[0].row].height = hVal / ROW_HEIGHT_RATIO # 行高を設定

    # Excelファイルを保存
    wb.save(inputFile)


#--- 全てのセルのフォント設定(引数指定) ---#
# inputFile:入力'.xlsxファイル'(.xlsxまでのパス)
# fontType:フォント名称
def SetDesignedFont(inputFile, fontType):
    #--- 変数宣言 ---#

    # Excelファイルを開く
    wb = openpyxl.load_workbook(inputFile)
    # アクティブなシートを取得する
    ws = wb.active

    # 全ての行高を設定
    for row in ws.iter_rows():
        for cell in row:
            cell.font = openpyxl.styles.Font(name=fontType) # フォントを設定

    # Excelファイルを保存
    wb.save(inputFile)


#--- Excelファイルにヘッダを挿入する ---#
# inputFile:入力'.xlsxファイル'(.xlsxまでのパス)
# headStrList:ヘッダ文字列リスト
def InsertHeader(inputFile, headStrList):
    #--- 変数宣言 ---#

    # Excelファイルを開く
    wb = openpyxl.load_workbook(inputFile)
    # アクティブなシートを取得する
    ws = wb.active

    # ヘッダを挿入
    ws.insert_rows(1)
    for col, header in enumerate(headStrList, start=1):
        ws.cell(row=1, column=col, value=header)

    # Excelファイルを保存
    wb.save(inputFile)


#--- Excelファイルの特定の列にフィルタを適用する ---#
# inputFile:入力'.xlsxファイル'(.xlsxまでのパス)
# colS:フィルタ対象スタート列
# colE:フィルタ対象エンド列
def ApplyFilter(inputFile, colS, colE):
    #--- 変数宣言 ---#

    # Excelファイルを開く
    wb = openpyxl.load_workbook(inputFile)
    # アクティブなシートを取得する
    ws = wb.active

    # フィルタをかける対象の列を指定
    colSLetter = openpyxl.utils.get_column_letter(colS)
    colELetter = openpyxl.utils.get_column_letter(colE)

    # フィルタをかける範囲を指定
    filterRange = f"{colSLetter}:{colELetter}"

    # フィルタを適用
    ws.auto_filter.ref = filterRange

    # Excelファイルを保存
    wb.save(inputFile)


#--- Excelファイルの特定セルでウィンドウを固定する ---#
# inputFile:入力'.xlsxファイル'(.xlsxまでのパス)
# colS:フィルタ対象スタート列
# areaVal:ウィンドウ枠固定セル位置
def UseFreezePanes(inputFile, areaVal):
    #--- 変数宣言 ---#

    # Excelファイルを開く
    wb = openpyxl.load_workbook(inputFile)
    # アクティブなシートを取得する
    ws = wb.active

    # 引数の値の位置でウィンドウ枠を固定
    ws.freeze_panes = areaVal

    # Excelファイルを保存
    wb.save(inputFile)


#--- main関数 ---#
def main():
    print("Youは本スクリプト：{}を直接実行しました".format(curScript))

if __name__ == "__main__":
    main()
