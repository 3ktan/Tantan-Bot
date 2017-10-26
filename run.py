import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import when_mentioned_or
import json
from tantanyan.utils import config

def load_extensions():
    with open("extensions.txt") as file:
        extensions = [e for e in file.read().splitlines() if e]
    for extension in extensions:
        try:
            bot.load_extension(extension)
            print("Loading",format(extension),"...Done")
        except Exception as e:
            print("Failed loading {}: {}".format(extension, e))



description="""
I am a bot written by 3ktan
"""


load = config.load_info()
token = load["token"]
prefix = load["prefix"]
bot = commands.Bot(command_prefix=when_mentioned_or(prefix), description=description)

@bot.event
async def on_ready():
    print("Logged in....")
    print("Name: {}".format(bot.user.name))
    print("ID: {}".format(bot.user.id))
    print("Discord version: ")
    print(discord.__version__)
    print("----------------------------")
    print("Loading module....Please wait")
    load_extensions()
    print("------------Loaded------------")
    await asyncio.sleep(5)
    await bot.change_presence(game=discord.Game(name='with 3ktan'))


bot.run(token)