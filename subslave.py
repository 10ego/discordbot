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

def get_gfycats(token, randomize = True, window=1000):
    random.seed(str(time.time()).split('.')[1])
    url = "https://api.gfycat.com/v1/gfycats/search?search_text={}".format(token)
    r = requests.get(url)
    tmp = r.json()
    size = min(tmp['found'], window)
    if randomize is True:
        rand = random.randrange(0, size)
    ##    cursor=''
    ##    for i in range(rand//10):
    ##        r=requests.get(url+"&count={}&cursor={}".format(10,cursor))
    ##        cursor = r.json()['cursor']
        r = requests.get(url+"&count={}".format(size))
        if r.status_code==200:
            gif_obj = r.json()
    ##        return gif_obj['gfycats'][rand%10]['max2mbGif']
    else:
        rand = random.randrange(0, size)
        r = requests.get(url+"&count={}".format(size))
        if r.status_code==200:
            gif_obj = r.json()
    return gif_obj['gfycats'][rand]['max2mbGif']

def get_games(limit=0):
    random.seed(str(time.time()).split('.')[1])
    games = {"League of Legends":{"player_limit": 5},
             "League of Legends(TFT)":{"player_limit":8},
             "Astroneer":{"player_limit":4},
             "Overwatch":{"player_limit":6},
             "Apex Legends":{"player_limit":3},
             "For the King":{"player_limit":3},
             "Don't Starve Together":{"player_limit":6},
             "Borderlands":{"player_limit":4},
             "Warhammer Vermintide 2":{"player_limit":4},
             "Risk of Rain 2":{"player_limit":4},
             "Monster Hunter: World":{"player_limit":16},
             "Terraria":{"player_limit":8}
             }
    if limit == 0:
        rand = random.randrange(0, len(games)-1)
        return list(games.keys())[rand]
    else:
        games = {k:v['player_limit'] for (k,v) in games.items() if v['player_limit']>=limit}
        rand = random.randrange(0, len(games)-1)
        return list(games.keys())[rand]
