import discord
from discord.ext import commands
import random
from .utils import check
import aiohttp
from tantanyan.utils import config
import  traceback
import asyncio

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

    #reload extension(s)
    @commands.command()
    @check.is_3ktan()
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

####################################################
    #change status
    @commands.command()
    @check.is_3ktan()
    async def status(self, ctx, *, stuff):
        await self.bot.change_presence(game=discord.Game(name=stuff))

    # logout!
    @commands.group(aliases=["out" ])
    @check.is_3ktan()
    async def logout(self, ctx):
        self.session.close()
        print("Thanks for the hard work!")
        await ctx.send("Thanks for the hard work!")
        self.session.close()
        await self.bot.logout()
####################################################################################

    #check bot's permission in a specific channel
    async def say_permissions(self, ctx, member, channel):
        permissions = channel.permissions_for(member)
        e = discord.Embed(title="Permissions of: " + member.name ,colour=member.colour)
        allowed, denied = [], []
        for name, value in permissions:
            name = name.replace('_', ' ').replace('guild', 'server').title()
            if value:
                allowed.append(name)
            else:
                denied.append(name)
        e.add_field(name='Allowed', value='\n'.join(allowed))
        e.add_field(name='Denied', value='\n'.join(denied))
        await ctx.send(embed=e)

    @commands.command(aliases=['botpermissions'])
    @check.mod_only()
    async def botper(self, ctx, *, channel: discord.TextChannel = None):
        channel = channel or ctx.channel
        member = ctx.guild.me
        # await ctx.send(member.name + "'s permissions:")
        await self.say_permissions(ctx, member, channel)

    @commands.command(aliases=['permissions'])
    @check.mod_only()
    async def userper(self, ctx, member: discord.Member = None, channel: discord.TextChannel = None):
        channel = channel or ctx.channel
        if member is None:
            member = ctx.author
        # await ctx.send(member.name + "'s permissions:")
        await self.say_permissions(ctx, member, channel)

    #delete message
    @commands.command(pass_context=True, aliases=['prune'], hidden=True)
    @check.mod_only()
    async def purge(self, ctx, *limit):
        try:
            limit = int(limit[0])
        except IndexError:
            limit = 1
        deleted = 0
        while limit >= 1:
            cap = min(limit, 100)
            deleted += len(await ctx.message.channel.purge( limit=cap, before=ctx.message))
            limit -= cap
        tmp = await ctx.send('**:put_litter_in_its_place:** {0} messages was deleted'.format(deleted))
        await asyncio.sleep(15)
        await self.bot.delete_message(tmp)
        await self.bot.delete_message(ctx.message)


def setup(bot):
    bot.add_cog(admiral(bot))