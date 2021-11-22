import token0

import discord
import json
from discord import Intents, channel, colour
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord import Embed
from discord.ext import commands
from discord.ext.commands import Bot as BotBase
from discord.ext.commands.core import check
from discord.ext.commands.errors import CommandNotFound
from discord.message import Message
from ygoprodeck import *
import random

client = commands.Bot(command_prefix='/')

@client.command()
async def doiget(ctx, *args):
    channel = client.get_channel(912106712457158697)
    
    choices = ["yes", "no"]
    
    ygo = YGOPro()
    name = " ".join(args[:])
    card_jibbler = ygo.get_cards(name=name)
    for element in card_jibbler['data']:
        ygo_card_deets = element
    value_random = random.choice(choices)

    embed = Embed(title="Card Name:", description=ygo_card_deets['name'])
    embed.add_field(name="Available: ", value=value_random, inline=False)
    await channel.send(embed=embed)

@client.command()
async def card(ctx, *args):
    channel = client.get_channel(912106439533801512)

    ygo = YGOPro()
    name = " ".join(args[:])
    card_jibbler = ygo.get_cards(name=name)
    for element in card_jibbler['data']:
        ygo_card_deets = element

    embed = Embed(title="Card Name:", description=ygo_card_deets['name'])
    embed.add_field(name="Card Type:", value=ygo_card_deets['type'], inline=False)
    try:
        if 'Link' in ygo_card_deets['type']:
            embed.add_field(name="Monster Link Rating:", value=ygo_card_deets['linkval'], inline=False)
            embed.add_field(name="Monster Type:", value=ygo_card_deets['race'], inline=False)
            embed.add_field(name="Monster Attribute:", value=ygo_card_deets['attribute'], inline=False)
            embed.add_field(name="Monster archetype:", value=ygo_card_deets['archetype'], inline=False)
            embed.add_field(name="Monster Attack:", value=ygo_card_deets['atk'], inline=False)
        if 'XYZ' or 'Fusion' or 'Synchro' or 'Pendulum' or 'Effect' or 'Tuner' or 'Normal' in ygo_card_deets['type']:
            embed.add_field(name="Monster Level:", value=ygo_card_deets['level'], inline=False)
            embed.add_field(name="Monster Type:", value=ygo_card_deets['race'], inline=False)
            embed.add_field(name="Monster Attribute:", value=ygo_card_deets['attribute'], inline=False)
            embed.add_field(name="Monster archetype:", value=ygo_card_deets['archetype'], inline=False)
            embed.add_field(name="Attack:", value=ygo_card_deets['atk'], inline=False)
            embed.add_field(name="Defense:", value=ygo_card_deets['def'], inline=False)
    except:
        pass
    embed.add_field(name="Card Description:", value=ygo_card_deets['desc'], inline=False)
    await channel.send(embed=embed)

@client.event
async def on_message(message):
    if message.channel.name == 'pack-opening' or 'ygo-card-info':
        await client.process_commands(message)


client.run(token0.token)