import discord
from discord.ext import commands
from tantanyan.utils import config, check


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




def setup(bot):
    bot.add_cog(Server_module(bot))