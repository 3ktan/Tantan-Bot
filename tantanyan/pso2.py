import discord
from discord.ext import commands
from tantanyan.utils import config


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



def setup(bot):
    bot.add_cog(Pso2(bot))