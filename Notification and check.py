#Brandon Bauer
#26-XX /9/2020
#Discord bot

import discord
import asyncio
from discord.ext import tasks
from Stock import getstock
import time

token='//////////////////'
stock  = 1
stockL = 1


client = discord.Client()

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
    print('check1')
    #stockL=getstock()
    while True:
        print('check2')
        #time.sleep(5)
        #stock=getstock()
        print('check3')
        if stockL==stock:
            stockL==stock
            print('check4')
            noti.start()
            client.run(token)

pingBauer()
