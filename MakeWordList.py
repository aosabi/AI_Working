# Janomeのインストール


# Janomeのロード
from janome.tokenizer import Tokenizer

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