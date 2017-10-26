import discord
from discord.ext import commands
# from cogs.utils.checks import embed_perms, cmd_prefix_len

'''Module for the >info command.'''


class Userinfo:

    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command=True, aliases=['user', 'info'])
    async def userinfo(self, ctx, *, name=""):
        """Get user info. Ex: >info @user"""
        if name:
            try:
                user = ctx.message.mentions[0]
            except:
                user = ctx.guild.get_member_named(name)
            if not user:
                user = ctx.guild.get_member(int(name))
            if not user:
                await ctx.send(self.bot.bot_prefix + 'Could not find user.')
                return
        else:
            user = ctx.message.author

        # Thanks to IgneelDxD for help on this
        if user.avatar_url[54:].startswith('a_'):
            avi = 'https://images.discordapp.net/avatars/' + user.avatar_url[35:-10]
        else:
            avi = user.avatar_url

        role = user.top_role.name
        if role == "@everyone":
            role = "None"
        voice_state = None if not user.voice else user.voice.channel
        em = discord.Embed(colour=0x708DD0)
        em.add_field(name='User ID', value=user.id, inline=True)
        em.add_field(name='Nickname', value=user.nick, inline=True)
        em.add_field(name='Status', value=user.status, inline=True)
        em.add_field(name='In Voice', value=voice_state, inline=True)
        em.add_field(name='Game', value=user.game, inline=True)
        em.add_field(name='Highest Role', value=role, inline=True)
        em.add_field(name='Account Created', value=user.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
        em.add_field(name='Join Date', value=user.joined_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
        em.set_author(name=user)
        em.set_thumbnail(url=avi)
        await ctx.send(embed=em)

    @commands.command()
    async def avatar(self, ctx, txt: str = None):
        """View bigger version of user's avatar. Ex: >info avi @user"""
        if txt:
            try:
                user = ctx.message.mentions[0]
            except:
                user = ctx.guild.get_member_named(txt)
            if not user:
                user = ctx.guild.get_member(int(txt))
            if not user:
                await ctx.send(self.bot.bot_prefix + 'Could not find user.')
                return
        else:
            user = ctx.message.author

        if user.avatar_url[54:].startswith('a_'):
            avi = 'https://images.discordapp.net/avatars/' + user.avatar_url[35:-10]
        else:
            avi = user.avatar_url
        em = discord.Embed(colour=0x708DD0)
        em.set_image(url=avi)
        await ctx.send(embed=em)



def setup(bot):
    bot.add_cog(Userinfo(bot))