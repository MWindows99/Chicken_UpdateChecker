#!/usr/bin/env python3
# coding: utf-8

# rss Update Checker
import feedparser
import tweepy
import os

# RSS
# ---Input youtube RSS URL---
url = 'https://www.youtube.com/feeds/videos.xml?channel_id=UCrM-4squf6A8iinZM1Li0Ig'
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
    # Update Found
    print("\n", subject)
    # Connect Twitter
    # ---Input your API Key---
    consumer_key ="xxxx"
    consumer_secret ="xxxx"
    access_token="xxxx"
    access_token_secret ="xxxx"
    # Create Object
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    # Tweet Content
    api.update_status("ちきんが動画を更新しました:" + subject + "URL: " + urls)
else:
    print("Updates is not found.")
