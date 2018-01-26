#!/usr/bin/env python
# Made by Multipixelone And PCC2
# MFKBot
import discord
import asyncio
import logging
from tokencord import tokencord
import datetime

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    #get_all_members()
    #print(server.members)

#@client.event
#async def on_message(message):
#    if message.content.lower().find('clut') > -1:
#        await client.delete_message(message)
#        await client.send_message(message.channel, '***GET THAT CANCER OUT OF HERE***')

@client.event
async def on_message(message):
    if message.content.startswith('$mfkstart'):
        await client.send_message(message.channel, '**Beginning a game of MFK!**')
        mfkstart = datetime.datetime.now()
    elif message.content.startswith('$mfkend'):
        await client.purge_from(message.channel, limit=500, after=mfkstart)
    elif message.content.lower().find('clut') > -1:
        await client.delete_message(message)
        await client.send_message(message.channel, '***GET THAT CANCER OUT OF HERE***')

client.run(tokencord)
