# Chicken_UpdateChecker
このスクリプトは、ChickenのYouTubeビデオの更新をチェックし、更新をTwitterに自動的に投稿します。

# ちきんは誰ですか
ちきんはとてもかわいい男の子です。

Twitter：[@chickenkundayo](https://twitter.com/chickenkundayo)

# 必要なライブラリ
## tweepy

```
pip3 install tweepy
```
  
## feedparser

```
pip3 install feedparser
```

# 実行前に
 - TwitterAPIキーをファイル内の指定された場所に書き加える必要があります。
 - 書き込み権限のあるディレクトリで実行してください。

# 実行方法
main.pyを実行すると自動的に動作します。 定期的に更新を確認するには、Cronに登録する必要があります。

## 例
以下の例では3時間おきに実行しています。

```
* */3 * * * python3 /home/USER/main.py
```
