from discord.ext import commands
import random
from tantanyan.utils import config, id
import discord.utils


#check admin or mod-who has permission
def is_owner(message):
    async def check_func(ctx):
        if ctx.message.author.id == id.admin_id:
            return True
        else:
            x = random.choice([ctx.author.mention + " go away",
                               "...Do not order me if you're not admin, "+ctx.author.mention,
                               "Don't touch me! :anger: ",
                               ":anger:  :anger:  :anger: "
                               ])
            await ctx.send(x)
            return False
    return commands.check(check_func)


def check_permissions(ctx, perms):
    msg = ctx.message
    if is_owner(msg):
        return True

    ch = msg.channel
    author = msg.author
    resolved = ch.permissions_for(author)
    return all(getattr(resolved, name, None) == value for name, value in perms.items())

def role_or_permissions(ctx, check, **perms):
    if check_permissions(ctx, perms):
        return True

    ch = ctx.message.channel
    author = ctx.message.author
    if ch.is_private:
        return False

    role = discord.utils.find(check, author.roles)
    return role is not None

def mod_only(**perms):
    async def predicate(ctx):
        x = random.choice([ctx.author.mention + ", you do not have permission to do that",
                           ])
        await ctx.send(x)
        return role_or_permissions(ctx, lambda r: r.name in ('Moderator', 'Admin'), **perms)

    return commands.check(predicate)

#check test server
def check_test_server(ctx):
    return ctx.guild.id==id.sever_test_id

def test_server_only():
	return commands.check(check_test_server)