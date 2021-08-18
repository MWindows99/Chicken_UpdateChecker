#!/usr/bin/env python3
# coding: utf-8

# rss更新確認スクリプト

import feedparser
import pprint
import time
import tweepy
import json
import os

url = 'https://www.youtube.com/feeds/videos.xml?channel_id=UCrM-4squf6A8iinZM1Li0Ig' # ちきんのYouTube RSS
feed = feedparser.parse(url)
subject = feed.entries[0].title
urls = feed.entries[0].link
new_up = feed.entries[0].updated

# Check File
local_path = "./feed.txt"
old_up = ""
if os.path.exists(local_path):
    with open(local_path) as f:
        old_up = f.read()
if (old_up != new_up):
    with open(local_path, mode='w') as f:
        f.write(new_up)
    # 更新があれば以下を実行
    # とりあえず画面に表示しておきますか
    print("\n", subject)
    # Twitter連携
    consumer_key ="xxxx"
    consumer_secret ="xxxx"
    access_token="xxxx"
    access_token_secret ="xxxx"
    # オブジェクト生成
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    # ツイート内容
    api.update_status("ちきんが動画を更新しました(test∞):" + subject + "URL: " + urls)
