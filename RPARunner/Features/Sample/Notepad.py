#!/usr/local/bin/python3
# coding: utf-8

###
# /* Notepad.py */
# 
# 
###

#--- モジュールのインポート ---#
import sys
import os
from subprocess import Popen
from pywinauto import Desktop

# プロジェクトのルートディレクトリをsys.pathに追加
#sys.path.append(os.path.join(os.path.dirname(__file__), '../../../'))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

#--- 自作モジュールのインポート ---#
from Utility import FileReadWriter, ExcelFileFormatter, FileManager, DataManager

#--- 変数宣言 ---#
curScript = sys.argv[0]

#--- main関数 ---#
def main():

    # メモ帳を起動
    Popen('notepad.exe', shell=True)

    # 最初に見つかったメモ帳を選択
    notepad = Desktop(backend="uia").window(title_re=".*メモ帳.*", found_index=0)

    # メモ帳ウィンドウが準備完了するまで待つ
    notepad.wait("ready")  # ウィンドウが準備完了するのを待つ

    # テキストエリアを操作
    text_area = notepad.child_window(control_type="Document")
    text_area.type_keys("明日、今日よりも好きになれる　溢れる想いが止まらない{ENTER}\
    今もこんなに好きでいるのに　言葉に出来ない{ENTER}\
    君のくれた日々が積み重なり　過ぎ去った日々2人歩いた『軌跡』{ENTER}\
    僕らの出逢いがもし偶然ならば？　運命ならば？{ENTER}\
    君に巡り合えた　それって『奇跡』{ENTER}\
    2人寄り添って歩いて　永久の愛を形にして{ENTER}\
    いつまでも君の横で　笑っていたくて{ENTER}\
    アリガトウや　Ah　愛してるじゃまだ足りないけど{ENTER}\
    せめて言わせて　「幸せです」と{ENTER}", pause=0.1)
    
    # 入力が完了するまで待機
    notepad.wait("ready")

    print("テキストを入力しました！")

if __name__ == "__main__":
    main()