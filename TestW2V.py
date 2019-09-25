import zipfile
from janome.tokenizer import Tokenizer



with zipfile.ZipFile(zip, 'r') as myzip:
    myzip.extractall()
    # 解凍後のファイルからデータ読み込み
    for myfile in myzip.infolist():
        # 解凍後ファイル名取得
        filename = myfile.filename
        # ファイルオープン時にencodingを指定してsjisの変換をする
        with open(filename, encoding='sjis') as file:
            text = file.read()

# ファイル整形
import re
# ヘッダ部分の除去
text = re.split('\-{5,}',text)[2]
# フッタ部分の除去
text = re.split('底本：',text)[0]
# | の除去
text = text.replace('|', '')
# ルビの削除
text = re.sub('《.+?》', '', text)
# 入力注の削除
text = re.sub('［＃.+?］', '',text)
# 空行の削除
text = re.sub('\n\n', '\n', text)
text = re.sub('\r', '', text)

# 整形結果確認

# 頭の100文字の表示
print(text[:100])
# 見やすくするため、空行
print()
print()
# 後ろの100文字の表示
print(text[-100:])



# Tokenneizerインスタンスの生成
t = Tokenizer()

# テキストを引数として、形態素解析の結果、名詞・動詞・形容詞(原形)のみを配列で抽出する関数を定義
def extract_words(text):
    tokens = t.tokenize(text)
    return [token.base_form for token in tokens
        if token.part_of_speech.split(',')[0] in['名詞', '動詞']]

#  関数テスト
# ret = extract_words('三四郎は京都でちょっと用があって降りたついでに。')
# for word in ret:
#    print(word)

# 全体のテキストを句点('。')で区切った配列にする。
sentences = text.split('。')
# それぞれの文章を単語リストに変換(処理に数分かかります)
word_list = [extract_words(sentence) for sentence in sentences]

# 結果の一部を確認
for word in word_list[0]:
    print(word)