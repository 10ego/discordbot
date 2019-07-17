import praw
import requests
import random
import time

### reddit ###
reddit = praw.Reddit(client_id="CLIENT_ID",
                     client_secret="CLIENT_SECRET",
                     user_agent="sub slavebot for slavebot (by /u/HELLOREDDIT)",
                     username="USERNAME",
                     password="PASSWORD")

reddit.read_only = True

def get_reddit(subreddit):
    subreddit = reddit.subreddit(subreddit)
    submission = subreddit.random()
    while submission.is_self:
        submission = subreddit.random()
    return submission.url

### gfycat ###

s = requests.session()

def get_gfycats(token):
    random.seed(str(time.time()).split('.')[1])
    url = "https://api.gfycat.com/v1/gfycats/search?search_text={}".format(token)
    r = requests.get(url)
    tmp = r.json()
    size = min(tmp['found'], 3000)
    rand = random.randrange(0, size)
##    cursor=''
##    for i in range(rand//10):
##        r=requests.get(url+"&count={}&cursor={}".format(10,cursor))
##        cursor = r.json()['cursor']
    r = requests.get(url+"&count={}".format(size))
    if r.status_code==200:
        gif_obj = r.json()
##        return gif_obj['gfycats'][rand%10]['max2mbGif']
        return gif_obj['gfycats'][rand]['max2mbGif']


