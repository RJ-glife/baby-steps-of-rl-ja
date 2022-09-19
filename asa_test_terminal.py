"""
9/19/2022 visual studio codeのTerminal利用のテスト

VSCodeの下に表示されるTerminalでCondaの仮想環境を作成した。
そこでファイルが実行されるかを確認する。
"""

import importlib
import sys
importlib.reload(sys) #再読み込み
print(sys.version_info)

print(
    "Python 3.6.13 :: Anaconda, Inc."
)
