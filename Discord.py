#Brandon Bauer
#26-XX /9/2020
#Discord bot

import discord
import asyncio
from Web_Scraping import Client
from discord.ext import tasks
from NewEgg_Stock import getstock
from Settings import token , url


stock  = 1
stockL = 1


client = discord.Client()
client_response = Client(url)

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
        
    if message.content.startswith('$Stop$'):
        noti.stop()
        await client.logout()

async def poke(message):
    member = discord.utils.get(client.get_all_members(),name='////')
    channel = await member.create_dm()
    await channel.send(message)
    
@tasks.loop(seconds=1.0)
async def noti():
    global stock
    await poke(stock)


@noti.before_loop
async def before_noti():
    print('waiting...')
    await client.wait_until_ready()


def pingBauer():
        noti.start()
        client.run(token)


stockL=getstock(client_response,url)
while True:
    print('check2')
    stock=getstock(client_response,url)
    print('check3')
    if stockL==stock:
        stockL=stock
        print('check4')
        pingBauer()
