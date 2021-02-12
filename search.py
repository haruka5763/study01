
### 検索ツールサンプル
### これをベースに課題の内容を追記してください

# 検索ソース
from abc import abstractproperty

source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]

### 検索ツール
def search():
    word =input("鬼滅の登場人物の名前を入力してください >>> ")
    
    ### ここに検索ロジックを書く

    if word in source:
        print("{}が見つかりました".format(word))
    else:
        print("{}は鬼滅の刃のキャラに含まれていません。追加しますか？".format(word))
        choice = input("Please respond with 'yes' or 'no' [y/N]: ").lower()
        if choice in ['y', 'ye', 'yes']:
            source.append(word)
            print("追加しました、こちらが新しいキャラのリスト一覧です！"+str(source))
        elif choice in ['n', 'no']:
            print("終了します")

if __name__ == "__main__":
    search()
