from discord.ext import commands
import random
from tantanyan.utils import config, id
import discord.utils

#check admin
def is_3ktan():
    async def check_func(ctx):
        if ctx.message.author.id == id.admin_id:
            return True
        else:
            x = random.choice([ctx.author.mention + " go away",
                               "...Do not order me if you're not 3ktan-chan, " + ctx.author.mention,
                               "Don't touch me! :anger: ",
                               ":anger:  :anger:  :anger: "
                               ])
            await ctx.send(x)
            return False
    return commands.check(check_func)

#check admin
def is_owner(message):
    async def check_func(ctx):
        if ctx.message.author.id == id.admin_id:
            return True
        else:
            return False
    return commands.check(check_func)

# check or mod-who has permission
def check_mod(ctx):
    return ctx.channel.permissions_for(ctx.message.author).manage_guild

def mod_only():
    return commands.check(check_mod)

#check test server
def check_test_server(ctx):
    return ctx.guild.id==id.sever_test_id

def test_server_only():
	return commands.check(check_test_server)