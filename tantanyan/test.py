import discord
from discord.ext import commands
from bs4 import BeautifulSoup
import codecs
import json
import aiohttp
import asyncio
import datetime
import os
import re
import random
from tantanyan.utils import config, id
import traceback

data = config.load_info()

class test:
    '''
    Test something here before using
    '''

    def __init__(self, bot):
        self.bot = bot
        self.sticker_regex = re.compile(r"(?<=[$+])\w+", flags=re.I)


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
    # @commands.command(name='pressf')
    # async def pressf(self, ctx, *, to: str=None):
    #     # await ctx.message.delete()
    #     if not to:
    #         to = "RIP"
    #     await ctx.send(f'**[Press F to {to}]**')
    #     msg = await ctx.send(':pressf:')
    #     await msg.add_reaction(u'👆')

    # @commands.command()
    # async def seach(self, ctx, *, name: str):
    #     data_embed =""
    #     try:
    #         with codecs.open("data/list_ship"+name+".json", encoding="utf-8") as file:
    #             jsonable = json.load(file)
    #             for key, value in jsonable.items():
    #                 data_embed = data_embed + str(key) + ": " + str(value) + "\n"
    #
    #             embed = discord.Embed()
    #             embed.set_thumbnail(url="https://vignette2.wikia.nocookie.net/kancolle/images/e/ee/DD_Akebono_Kai_231_Card.jpg/revision/latest?cb=20161209135150")
    #             embed.add_field(
    #                 name="Here, it's the information analysis. ",
    #                 value=data_embed
    #             )
    #             embed.set_image(url="http://kancolle.wikia.com/wiki/Akebono?file=DD_Akebono_Kai_231_Card.jpg")
    #             await ctx.send(embed=embed)
    #     except:
    #         await ctx.send("No data.")

    # @commands.command( aliases=[""])
    # async def emo(self, ctx):
    #     keys = ("Icon_HP", "Icon_Armor", "Icon_Evasion")
    #     emoji = {}
    #     test_guild = self.bot.get_guild(id.sever_test_id)
    #     for key in keys:
    #         emoji[key] = discord.utils.find(lambda e: e.name == key, test_guild.emojis)
    #     msg = await ctx.send(embed=discord.Embed(
    #         description=f"{emoji['Icon_HP']} HP: 15\n{emoji['Icon_Armor']} Armor: 6 (19)\n{emoji['Icon_Evasion']} Evasion: 42 (79)"))
    #     await msg.add_reaction(u'👆')


    # @commands.command( )
    # async def s(self, ctx):
    #     avi="https://vignette.wikia.nocookie.net/kancolle/images/f/f1/CL_Abukuma_114_Full.png/revision/latest?cb=20150519031352"
    #     embed = discord.Embed()
    #     em = discord.Embed(
    #         title="Full Size",
    #         url=avi,
    #         colour=0x708DD0
    #     )
    #     embed.set_image(url=avi)
    #     await ctx.send(embed=embed)

    # # test sau
    # @commands.command()
    # async def cat(self, ctx):
    #     await ctx.channel.trigger_typing()
    #     cat.getCat(directory="data", filename="cat", format="gif")
    #     await asyncio.sleep(1)  # This is so the bot has enough time to download the file
    #     await ctx.send(file=discord.File("data/cat.gif"))

    #test sau
    # @commands.command()
    # async def quote(self, ctx):
    #     """Don't quote me on that"""
    #     await ctx.channel.trigger_typing()
    #     await ctx.send(file=discord.File("assets/imgs/quotes/{}.png".format(
    #         random.randint(1, len([file for file in os.listdir("assets/imgs/quotes")])))))





def setup(bot):
    bot.add_cog(test(bot))