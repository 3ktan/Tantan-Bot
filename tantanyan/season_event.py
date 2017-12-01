import discord
from discord.ext import commands
from bs4 import BeautifulSoup
from datetime import *
import json
import aiohttp
import datetime
import io
import re
import random

from tantanyan.utils import config

christmas = date(datetime.datetime.now().year, 12, 25)
daystillchristmas = (christmas - date.today()).days
if daystillchristmas < 0:
    christmas = date(datetime.datetime.now().year + 1, 12, 25)
    daystillchristmas = (christmas - date.today()).days

# daystillchristmas = (christmas - date.today()).days
class Season_event:
    '''
    some lines for season event of Tantanyan-chan
    '''
    def __init__(self, bot):
        self.bot = bot
        self.now = date.today()

    #Christmas
    # @commands.group()
    # async def xmas(self, ctx ):
    #     if ctx.invoked_subcommand is None:
    #         # timestamp = ctx.message.created_at
    #         timestamp = datetime.datetime.now()
    #         print(timestamp)
    #         if (str(timestamp.day) == "28" and str(timestamp.month) == "10"):
    #             if timestamp.hour < 21:
    #                 x = random.choice([
    #                     # "Christmas? That has nothing to do with me, though. ...But well, I'll still have some cake... alright?",
    #                     "Hehe, I will receive gifts from Santa tonight! | Waaa, Shit-Shitty Admiral? :bangbang: | Stay away from me!! :anger:",
    #                     # "W-what is it?",
    #                 ])
    #                 await ctx.send(x)
    #             else:
    #                 if self.now.hour > 22:
    #                     x = random.choice([
    #                         "Zzzz....Zzzzz....",
    #                         "",
    #                         "What is it?",
    #                     ])
    #                     result = True
    #                     await ctx.send(x)

# OTHER ###############################################################################################################
    # Hi
    @commands.command(aliases=["hello","Hello","Hi",
                               "konnichiwa","Konnichiwa","ohayo","Ohayo","konbanwa","Konbanwa",
                               "Yo","yo","Ya","ya"])
    async def hi (self, ctx):
        now = datetime.datetime.now().hour
        if now >=0 and now <=6:
            x = random.choice(["Zzz...zzz...",
                               ])
        elif now in range(6,13):
            x = random.choice(["Ohayo",
                               "Ohayo "+ctx.author.mention,
                               ])
        elif now in range(12,19):
            x = random.choice(["Konnichiwa",
                               ])
        else:
            x = random.choice(["Konbanwa",
                               ])
        await ctx.send(x)
################################################################################################################
    # Christmas
    @commands.group(aliases=["xmas","noel"])
    async def christmas(self, ctx):
        if ctx.invoked_subcommand is None:
            if daystillchristmas >7:
                x = random.choice(["{} days to the Christmas".format(daystillchristmas),
                                    "1, 2, 3,....still {} days left until the Christmas".format(daystillchristmas),

                               ])
                await ctx.send(x)
            elif daystillchristmas <= 7 and daystillchristmas >=1:
                x = random.choice(["There are only {} days left until the Christmas!! Ò v Ó".format(daystillchristmas),
                                    "Awwww, I can't wait! {} days to Christmas!".format(daystillchristmas),
                                   "I hope i will have a Christmas present\n"
                               ])
                await ctx.send(x)
            else:
                x = random.choice(["https://i.imgur.com/aX1qmqU.png",
                                "https://media.giphy.com/media/lmsRHBoMSXDm8/giphy.gif"
                               ])
                embed = discord.Embed()
                embed.set_image(url=x)
                await ctx.send(embed=embed)

    @christmas.command()
    async def gift(self, ctx):
        if ctx.invoked_subcommand is None:
            if daystillchristmas == 0:
                x = random.choice(["Thank you, but it's not Christmas yet",
                                    "Errrrr....? Thanks, but there are {} days left until the Christmas.".format(daystillchristmas),

                               ])
                await ctx.send(x)
            else:
                x = random.choice(["https://i.imgur.com/aX1qmqU.png",
                                "https://media.giphy.com/media/lmsRHBoMSXDm8/giphy.gif"
                               ])
                embed = discord.Embed()
                embed.set_image(url=x)
                await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Season_event(bot))
