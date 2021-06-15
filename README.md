# make-dialogue-corpus
対話破綻検出チャレンジに使用されている[雑談対話コーパス](https://sites.google.com/site/dialoguebreakdowndetection/chat-dialogue-corpus)を使って対話ペアデータを作成するためのツールです。

# 必要なもの
python 3.x系  
(当環境はpython3.9.5)

# 生成されるもの
生成されるファイル（source.txt, target.txt）はdbdcディレクトリに、ダウンロードしたデータはrawディレクトリに入ります。  
source.txtには対話ペアデータの入力文、target.txtには対話ペアデータの出力文が格納されます。それぞれのファイルの同行の文が対となっている形になります。

# 使い方の例
```bash
git clone <URL>
cd make-dialogue-corpus
python3 main.py
```

# 注意点
対話ペアデータを作る際には、対話破綻していない対話ペアデータのみを取り出してデータセットを作成しました。  
この雑談対話コーパスでは、各発話応答に対して数人が「対話破綻しているか否か」のアノテーションをつけているので、そのアノテーションを参照して半数以上が「対話破綻していない」と判断している対話ペアのみを採用しています。

# ライセンス
作成されたコーパスは元データである雑談対話コーパスのライセンスに準じますので、詳しくはrawディレクトリにあるライセンスをご確認ください。  
以下、[対話破綻検出チャレンジ 3.雑談対話コーパスのライセンス](https://sites.google.com/site/dialoguebreakdowndetection/chat-dialogue-corpus)より引用  
>本データはMITライセンスのもと，無償・無保障にて研究用・商用を問わず利用できます．ただし，本データを利用して得た成果を学会等で発表する際には，可能な限り，本データについての以下の報告・論文を引用するとともに，NTTドコモの雑談対話APIへの参照をお願いします．詳細は本コーパスに同梱されているライセンスをご覧ください．