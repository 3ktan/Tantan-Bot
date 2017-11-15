import discord
from discord.ext import commands
from tantanyan.utils import config, check
import random



class Server_module:
    def __init__(self, bot):
        self.bot = bot

    #about server
    @commands.command()
    async def server(self, ctx):

        avt = ctx.guild.icon_url
        embed = discord.Embed(
            title=ctx.guild.name,
            colour=discord.Colour.teal(),
            icon_url=ctx.guild.icon_url_as(format='png')
        )
        embed.add_field(
            name="Owner",
            value=ctx.guild.owner,
            inline=True
        )
        embed.add_field(
            name="Region",
            value=ctx.guild.region,
            inline=True
        )
        embed.add_field(
            name="Server's Id",
            value=ctx.guild.id,
            inline=True
        )
        embed.add_field(
            name="Number of menber",
            value=ctx.guild.member_count,
            inline=True
        )
        embed.add_field(
            name="Afk Channel",
            value=ctx.guild.afk_channel,
            inline=True
        )
        embed.add_field(
            name="Created At",
            value=ctx.guild.created_at,
            inline=True
        )
        await ctx.send(embed=embed)

    #server's icon
    @commands.command()
    async def servericon(self, ctx):
        avt=ctx.guild.icon_url
        embed = discord.Embed(
            title= "Server's icon: " + ctx.guild.name,
            url=avt
        )
        embed.set_image(url=ctx.guild.icon_url_as(format='png'))
        await ctx.send(embed=embed)

    #kick someone
    @commands.command()
    @check.mod_only()
    async def kick(self, ctx, user:discord.Member):
        try:
            await ctx.guild.kick(user)
            x = random.choice(["`{}` has been kicked".format(user),
                               "Too bad, `{}` has been kicked".format(user),
                               "`{}` did something bad, so he/she has been kicked".format(user),
                               f"Prepare to be kicked, `{format(user)}`-san. Oupssss, `{format(user)}` has been kicked... Tee-hee~",
                               "Time to KICK!!! `{}` will be in favor of the first".format(user)
                               ])
            await ctx.send(x)
        except discord.errors.Forbidden:
            if user.top_role.position == ctx.me.top_role.position:
                x = random.choice(["{}, I can't kick them, because they have the same role as me!".format(ctx.author.mention),
                                   "I need higher role to do that. ( ≧Д≦)",
                                   "Did you ever know that I can't really kick that user just simply because it's on the same role level as me? (；￣Д￣）",

                                   ])
                await ctx.send(x)
            elif user.top_role.position > ctx.me.top_role.position:
                x = random.choice(["Their role is higher than me!",
                                    "Their role is too high (,,#ﾟДﾟ)",
                                   "My role is too low to kick them! OAO",
                                   ])
                await ctx.send(x)
            else:
                x = random.choice(["I don't have the `Kick Members` permission... <_<",
                                    "I don't have permission to kick anyone! '_'",
                                   "{}, you have to give me permission to kich them".format(ctx.author.mention),
                                   "Come on, if {}-chan don't give me permission, I can't kick anyone out. ｍ（＿　＿；；ｍ".format(ctx.author.mention),
                                   "Wanna kick someone? Give me permission, first! OAO",
                                   "`Kick Members`, I want that! :\"<",
                                   "https://i.imgur.com/QJrmy3N.png"
                                   ])
                await ctx.send(x)

    #ban member
    @commands.command()
    @check.mod_only()
    async def ban(self, ctx, user: discord.Member, *, reason: str = None):
        if reason is None:
            x = random.choice(["You can not ban someone without reason, {}".format(ctx.author.mention),
                               "Ban someone with no reason? No! You can't Ò^Ó",
                               "I need a reason to ban someone!",
                               "I am sure they will not accept if you kick them for no reason!"
                               ])
            await ctx.send(x)
        else:
            try:
                await ctx.guild.ban(user, delete_message_days=0, reason=reason)
                x = random.choice([f"`{format(user)}` has been banned because: \"`{reason}`\" ",
                                   f"{format(ctx.author.mention)} had baned `{format(user)}` with reason: `{reason}`",
                                   f"For `{reason}` reason, `{format(user)}` will be on the server's banlist!",
                                   f"1 minute silent, `{format(user)}` have been kicked because: `{reason}`"
                                   ])
                await ctx.send(x)
            except discord.errors.Forbidden:
                if user.top_role.position == ctx.me.top_role.position:
                    x = random.choice(["{}, I can't kick them, because they have the same role as me!".format(ctx.author.mention),
                                        "I need higher role to do that. ( ≧Д≦)",
                                        "Did you ever know that I can't really kick that user just simply because it's on the same role level as me? (；￣Д￣）",
                                       "Can't ban someone if they're on the same level as I am. "
                                       ])
                    await ctx.send(x)
                elif user.top_role.position > ctx.me.top_role.position:
                    x = random.choice(["I can't ban someone if they're higher than me, fool!",
                                       "Their role is too high (,,#ﾟДﾟ)",
                                       "I can not do anything with a low role like this! (╯°□°）╯︵ ┻━┻ ",
                                       "I need higher role! (╯°□°）╯"
                                       ])
                    await ctx.send(x)
                else:
                    x = random.choice(["Can't smash someone with a ban hammer if I don't even have the `Ban Members` permission.",
                                       "I don't have the `Kick Members` permission... <_<",
                                       "I don't have permission to ban anyone! '_'",
                                       "{}, you have to give me permission to ban them".format(ctx.author.mention),
                                       "Come on, if {}-chan don't give me permission, I can't ban anyone. ｍ（＿　＿；；ｍ".format(ctx.author.mention),
                                       "Wanna ban someone? Give me permission, first! OAO",
                                       "`Ban Members`, I want that! :\"<",
                                       "https://i.imgur.com/QTlFbZl.png",
                                       ])
                    await ctx.send(x)
                return

    #unban
    #sonething went wrong........
    @commands.command()
    @check.mod_only()
    async def unban(self, ctx, *, username: str):
        try:
            banlist = await ctx.guild.bans()
        except discord.errors.Forbidden:
            x = random.choice({"I don't have the `Ban Members` permission... <_<",
                               "I don't have permission to unban anyone! '_'",
                               "{}, you have to give me permission to unban them".format(ctx.author.mention),
                               "Come on. How can i unban someone if i don't have Ban Member permission? ｍ（＿　＿；；ｍ",
                               "Wanna unban someone? Give me permission, first! OAO",
                               "`Ban Members`, I need that! :\"<",
                               "https://i.imgur.com/QTlFbZl.png",
                               })
            await ctx.send(x)
            return
        user = None
        for ban in banlist:
            ctx.send(ban)
            # if ban.user.name == username:
            #     user = username
            #     break
        # if user is None:
        #     x = random.choice([f"For somewhat reason, `{format(username)}` isn't on the banlist.",
        #                        f"`{format(username)}` is not on the banlist",
        #                        "No one has that name on banlist, please check again",
        #                        ])
        #     await ctx.send(x)
        #     return
        # await ctx.guild.unban(user)
        # await ctx.send("Pardoned `{}`.".format(user))

    #Displays the server's banlist
    @commands.command()
    @check.mod_only()
    async def banlist(self, ctx):
        try:
            banlist = await ctx.guild.bans()
        except discord.errors.Forbidden:
            x = random.choice(["I don't have the `Ban Members` permission... \">_>",
                               "Can't list them without the `Ban Members` permission.",
                               "`Ban Members`, I need that to show banlist! :\"<",
                               "https://i.imgur.com/QTlFbZl.png",
                               ])
            await ctx.send(x)
            return
        bancount = len(banlist)
        display_bans = []
        bans = None
        if bancount == 0:
            bans = "No one's banned."
        else:
            for ban in banlist:
                if len(", ".join(display_bans)) < 1800:
                    display_bans.append(str(ban.user))
                else:
                    bans = ", ".join(display_bans) + "\n... and {} more".format(len(banlist) - len(display_bans))
                    break
        if not bans:
            bans = ", ".join(display_bans)
        await ctx.send("Total bans: `{}`\n```{}```".format(bancount, bans))

def setup(bot):
    bot.add_cog(Server_module(bot))