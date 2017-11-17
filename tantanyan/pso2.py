import discord
from discord.ext import commands
from tantanyan.utils import config
import aiohttp
import json

class Pso2:
    def __init__(self, bot):
        self.bot = bot
    '''
    Phantasy Star Online 2: http://pso2.jp/players/
    '''
    @commands.group()
    async def pso2(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("Link Related \n"
                           "Newbie: <https://goo.gl/Z5UnRq> \n"
                           "Mag: <https://goo.gl/qUuXE1> \n"
                           "Skill tree: <https://goo.gl/JtZmeL> \n"
                           "Swiki: <http://pso2.swiki.jp/index.php> \n"
                           "Bumped: <http://www.bumped.org/psublog/> \n"
                           "PSO2 Affixing Simulator: <http://pso2affix.seilent.net/>\n")

    # @pso2.command()
    # async def newbie(self,ctx):
    #     await ctx.send("https://goo.gl/Z5UnRq")
    @commands.command(pass_context=True)
    async def item(self, ctx, *, itemname : str):
        async with aiohttp.ClientSession() as session:
            url = "http://db.kakia.org/item/search?name={0}".format(itemname.replace(" ", "%20"))
            r = await session.get(url)
            if r.status == 200:
                js = await r.json()
                embed = discord.Embed()
                if js:
                    if len(js) >= 1 and len(js) <= 10:
                        for result in js:
                            if result["EnName"]:
                                endesc = result['EnDesc'].replace("\n", "")
                                embed.add_field(
                                    name="Resuilts:",
                                    value=f"**EN Name:** {format(result['EnName'])} - **JP Name:** {format(result['JpName'])}\n"
                                            f"**Desc:** {endesc} \n "
                                )
                        await ctx.send(embed=embed)
                    elif len(js) > 10:
                        await ctx.send("{} Found too many items matching {}. Please try a more specific search.".format(ctx.message.author.mention, itemname))
                else:
                    await ctx.send("{} Could not find ``{}``.".format(ctx.message.author.mention, itemname))

    @commands.command(pass_context=True)
    async def price(self, ctx, *, itemname: str):
        async with aiohttp.ClientSession() as session:
            url = "http://db.kakia.org/item/search?name={0}".format(itemname.replace(" ", "%20"))
            r = await session.get(url)
            if r.status == 200:
                js = await r.json()
                embed = discord.Embed()
                if js:
                    if len(js) >= 1 and len(js) <= 10:
                        for result in js:
                            if result["EnName"]:
                                embed.add_field(
                                    name="Success",
                                    value=ctx.author.mention,
                                    inline=False
                                )
                                embed.add_field(
                                    name="Searched for:",
                                    value=f"**EN Name:** {format(result['EnName'])} \n**JP Name:** {format(result['JpName'])}"
                                )
                            if result['PriceInfo'] is not None:
                                pri = "\n"
                                for PriceInfo in result['PriceInfo']:
                                    pri  = pri + "Ship `" + format(PriceInfo['Ship']) + "`  :   " + format(PriceInfo['Price'],',d')+ "                     - Last Updated: " + format(PriceInfo['LastUpdated']) + "\n"
                                embed.add_field(
                                    name="Cheapest from each ship:",
                                    value=pri,
                                    inline=False
                                )
                            else:
                                embed.add_field(
                                    name="Price: ",
                                    value="Unknown",
                                    inline=False
                                )

                        await ctx.send(embed=embed)
                    elif len(js) > 10:
                        await ctx.send("{} Found too many items matching {}. Please try a more specific search.".format(ctx.message.author.mention, itemname))
                else:
                    await ctx.send("{} Could not find ``{}``.".format(ctx.message.author.mention, itemname))


def setup(bot):
    bot.add_cog(Pso2(bot))