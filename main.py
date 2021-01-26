import requests
import discord
import re
from utils import *
import random

token = open('discordtoken.txt', 'r').readline()
#print(token)
client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    #print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
    
    if message.content=="!help":
        help_msg = "!togethertube, !ping, !gif {keyword}, !duck, !react, !waifu, !zoidberg, !got, !alan, !whattoplay {max player #}, !rand {number1 number2}"
        await message.channel.send(help_msg)

    elif message.content=="!togethertube":
        s = requests.Session()
        base_url = "https://togethertube.com"
        r = s.get(base_url+"/room/create")
        if r.status_code==200:
#            rr = s.get(r.url)
#            s.headers
#            h = {}
            await message.channel.send(r.url)
            
    elif re.match(r"\!ping \<\@\S+\>", message.content):
        at = re.search("\<\@\S+\>", message.content).group(0)
        await message.channel.send(f":speaking_head: Ping Ping Ping Ping Ping {at}")

    elif re.fullmatch(r"\!gif", message.content):
        switch=True
        while switch is True:
            link = get_reddit('gif')
            if "gif" in link[-4:]:
                await message.channel.send(link)
                switch = False
    elif re.fullmatch(r"\!rand \d+ \d+", message.content):
        random_numbs = re.findall(r"\d+", message.content)
        await message.channel.send("Randomly chosen number: {}".format(random.randrange(int(min(random_numbs)), int(max(random_numbs)))))
            
    elif re.match(r"\!gif .*", message.content):
        q_term = message.content[5:].replace(" ", "+")
        print(q_term)
        await message.channel.send(get_gfycats(q_term))

    elif re.fullmatch(r"\!duck", message.content):
        await message.channel.send(get_reddit('duckswithanimeeyes'))
        
    elif re.fullmatch(r"\!react", message.content):
        await message.channel.send(get_reddit('reactiongifs'))
        
    elif re.fullmatch(r"\!waifu", message.content):
        await message.channel.send(get_gfycats('funimation+waifu+anime'))
        
    elif re.fullmatch(r"\!zoidberg", message.content):
        await message.channel.send(get_gfycats('zoidberg'))
        
    elif re.fullmatch(r"\!got", message.content):
        await message.channel.send(get_gfycats('game+of+thrones'))
#    print(f'{message.channel}: {message.author}: {message.author.name}: {message.content}')

    elif re.fullmatch("!alan", message.content):
        await message.channel.send(get_gfycats("alan+groundhog", randomize=False, window=17))
        
    elif re.fullmatch("!whattoplay\s?\d*", message.content):
        if len(message.content)>11:
            player_size = int(message.content[12:])
        else:
            player_size = 0
        await message.channel.send(get_games(player_size))
        
client.run(token.strip())


