#!/usr/bin/env python
# Made by Multipixelone And PCC2
# MFKBot
import discord
import asyncio
import logging
from tokencord import tokencord

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

#@client.event
#async def on_message(message):
#    if message.content.lower().find('clut') > -1:
#        await client.delete_message(message)
#        await client.send_message(message.channel, '***GET THAT CANCER OUT OF HERE***')

@client.event
async def on_message(message):
    if message.content.startswith('$mfk'):
        await client.send_message(message.channel, '**Beginning a game of MFK!**')
    elif message.content.lower().find('clut') > -1:
        await client.delete_message(message)
        await client.send_message(message.channel, '***GET THAT CANCER OUT OF HERE***')

client.run(tokencord)
