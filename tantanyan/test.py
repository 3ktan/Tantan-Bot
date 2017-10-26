import discord
from discord.ext import commands
from bs4 import BeautifulSoup
import codecs
import json
import aiohttp
import datetime
import io
import re
import random
from tantanyan.utils import config

class test:
    '''
    Test something here before using
    '''

    def __init__(self, bot):
        self.bot = bot
        self.sticker_regex = re.compile(r"(?<=[$+])\w+", flags=re.I)

    @commands.command()
    async def jj(self,ctx):
        data = config.load_info()
        print(data["token"])

    #on_message
    async def on_message(self, message):
        if message.author.bot:
            return
        result = self.sticker_regex.findall(message.content)
        # await message.channel.send(result)
        text_clgt =  ["'clgt'", "'clg'"]
        clgt = "https://i.imgur.com/I3FY2Jd.png"
        if result != []:
            print(result)
            if text_clgt[0] in result:
                embed = discord.Embed( )
                embed.set_image(url=clgt)
                await message.channel.send(embed=embed)

    #add reaction
    @commands.command(name='pressf')
    async def pressf(self, ctx, *, to: str=None):
        # await ctx.message.delete()
        if not to:
            to = "RIP"
        await ctx.send(f'**[Press F to {to}]**')
        msg = await ctx.send(':pressf:')
        await msg.add_reaction(u'👆')

    @commands.command()
    async def seach(self, ctx, *, name: str):
        data_embed =""
        try:
            with codecs.open("data/list_ship"+name+".json", encoding="utf-8") as file:
                jsonable = json.load(file)
                for key, value in jsonable.items():
                    data_embed = data_embed + str(key) + ": " + str(value) + "\n"

                embed = discord.Embed()
                embed.set_thumbnail(url="https://vignette2.wikia.nocookie.net/kancolle/images/e/ee/DD_Akebono_Kai_231_Card.jpg/revision/latest?cb=20161209135150")
                embed.add_field(
                    name="Here, it's the information analysis. ",
                    value=data_embed
                )
                embed.set_image(url="http://kancolle.wikia.com/wiki/Akebono?file=DD_Akebono_Kai_231_Card.jpg")
                await ctx.send(embed=embed)
        except:
            await ctx.send("No data.")

def setup(bot):
    bot.add_cog(test(bot))