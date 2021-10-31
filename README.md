# Chicken_UpdateChecker
Can't read English? Please check the Japanese edition: [Readme Japanese](README_JA.md)

This script checks for updates to Chicken's YouTube video and automatically posts any updates on Twitter.

# Who is Chicken
He is very cute boy.

Twitter:[@chickenkundayo](https://twitter.com/chickenkundayo)

# Need to Install
## tweepy

```
pip3 install tweepy
```

## feedparser

```
pip3 install feedparser
```

# Before run
 - You need to insert the Twitter API key in the specified location in the file.

 - Execute it in a directory to which you have write permission.

# How to Run
It works automatically when you run main.py. You must register with Cron to check for updates on a regular basis.

## Example
In the example below, it runs every 3 hours.

``` 
* */3 * * * python3 /home/USER/main.py
```
