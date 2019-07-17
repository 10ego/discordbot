import requests
import discord
import re
from subslave import *

token = open('discordtoken.txt', 'r').readline()
#print(token)
client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
    
    if message.content=="!help":
        help_msg = "!togethertube, !ping, !gif, !duck, !react, !waifu, !zoidberg"
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

    elif re.match(r"\!gif", message.content):
        await message.channel.send(get_reddit('gif'))

    elif re.match(r"\!duck", message.content):
        await message.channel.send(get_reddit('duckswithanimeeyes'))
        
    elif re.match(r"\!react", message.content):
        await message.channel.send(get_reddit('reactiongifs'))
        
    elif re.match(r"\!waifu", message.content):
        await message.channel.send(get_gfycats('funimation+waifu+anime'))
        
    elif re.match(r"\!zoidberg", message.content):
        await message.channel.send(get_gfycats('zoidberg'))
        
    elif re.match(r"\!got", message.content):
        await message.channel.send(get_gfycats('game+of+thrones'))
#    print(f'{message.channel}: {message.author}: {message.author.name}: {message.content}')

client.run(token.strip())


