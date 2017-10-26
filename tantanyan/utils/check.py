from discord.ext import commands
import random
from tantanyan.utils import config

data = config.load_info()

def is_owner():
    async def check_func(ctx):
        if str(ctx.message.author.id) == data["admin_id"]:
            return True
        else:
            x = random.choice([ctx.author.mention + " go away",
                               "...",
                               "Don't touch me! :anger: ",
                               ":anger:  :anger:  :anger: "
                               ])
            await ctx.send(x)
            return False
    return commands.check(check_func)


