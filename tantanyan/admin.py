import discord
from discord.ext import commands
import random
from .utils import check
import aiohttp
from tantanyan.utils import config
import  traceback

class admiral:
    def __init__(self,bot):
        self.bot = bot
        self.session = aiohttp.ClientSession(loop=self.bot.loop, headers={"User-Agent": "AppuSelfBot"})

########################## FUNCTIONS ##########################
    #reload one extension
    def reload_extension(self, extension):
        try:
            self.bot.unload_extension(extension)
            self.bot.load_extension(extension)
            print("Reloading " + extension + "...Done'")
        except Exception as e:
            print("Failed reloading {}:\n{}".format(extension, traceback.format_exc()))

    # reload all extension
    def reload_all_extensions(self):
        with open("extensions.txt") as file:
            extensions = [e for e in file.read().splitlines() if e]
        for extension in extensions:
            self.bot.unload_extension(extension)
        for extension in extensions:
            try:
                self.bot.load_extension(extension)
                print("Reloading " + extension + "...Done")
            except Exception as e:
                print("Failed reloading {}:\n{}".format(extension, traceback.format_exc()))

########################## ADMIN COMMANDS ##########################
    #reload extension(s)
    @commands.command()
    @check.is_owner()
    async def rl(self, ctx, extension: str = ""):
        self.session.close()
        print("Reloading module(s)...Please wait")
        if extension != "":
            await ctx.send("Reloading `"+ extension + "`...Please wait")
            extension = "tantanyan." + extension
            self.reload_extension(extension)
        else:
            await ctx.send("Reloading `all` extensions...Please wait")
            self.reload_all_extensions()
        print("All Done.")
        print("----------------------------")
        await ctx.send("Done")

    #change status
    @commands.command()
    @check.is_owner()
    async def status(self, ctx, *, stuff):
        await self.bot.change_presence(game=discord.Game(name=stuff))

    # logout!
    # What lies at the bottom of the sea...?
    @commands.group(aliases=["out" ])
    @check.is_owner()
    async def logout(self, ctx):
        self.session.close()
        print("Thanks for the hard work!")
        await ctx.send("Thanks for the hard work!")
        await self.bot.logout()



def setup(bot):
    bot.add_cog(admiral(bot))