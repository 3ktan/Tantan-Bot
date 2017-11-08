import discord
from discord.ext import commands
from tantanyan.utils import config, check


class Help_module:
    def __init__(self, bot):
        self.bot = bot
        self.bot.remove_command("help")

    @commands.group()
    async def help(self, ctx ):
        if ctx.invoked_subcommand is None:
            embed = discord.Embed(
                title=self.bot.user.name,
                colour=discord.Colour.teal(),
                description="Description: Phantasy Star Online 2 & Kantai Collection (kancolle)")
            embed.add_field(
                name="Standard Commands List ",
                value="`//mod`: commands for mod\n"
                      "`//inv`: Invite bot to your server\n"
                      "`//about:` description about Bot & Athor\n"
                      "`//help user:` Get information about a user \n"
                      "`//help server:` Get information about a server \n"
                      "`//help meme`: List meme\n"
                      "`//help pso2`: Phantasy Star Online 2\n"
                      "`//help other`: Some stupid things _(:3 \n"
                      "`//help translate`: Translation to multiple languages \n"
                      "")
            await ctx.send(embed=embed)


    @commands.command()
    async def inv(self, ctx):
        embed = discord.Embed(
            colour=discord.Colour.teal(),
            )
        embed.add_field(
            name="Invite Link:",
            value="https://goo.gl/VM2xRn"
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def about(self, ctx):
        embed = discord.Embed(
            title=self.bot.user.name,
            colour=discord.Colour.teal(),
            description="About bot: A tsundere bot. She like Pso2 & Kankolle. \n"
                        "Support: https://discord.gg/86SXwYJ \n"
                        "Invite bot to your server: https://goo.gl/VM2xRn"
        )
        embed.add_field(
            name="Athor: 3ktan",
            value="Facebook: https://www.facebook.com/3ktan/\n"
                  "Wordpress: http://3ktan.wordpress.com/\n"
                  "Twitter: https://twitter.com/3ktan/",
            inline=False
        )
        embed.set_thumbnail(
            url="https://i.imgur.com/nBpePWb.png"
        )
        await ctx.send(embed=embed)

    @help.command()
    @check.mod_only()
    async def mod(self, ctx):
        embed = discord.Embed(
            colour=discord.Colour.teal(),
        )
        embed.add_field(
            name="Server:",
            value=  "`//kick @someone`: kick someone out the server\n"
                    "`//ban @someone reason`: you need a reason before you ban anyone\n"
                    "`//unban @sonmeone`: unban someone\n"
                    "`//banlist`: server's banlist"
        )
        await ctx.send(embed=embed)

    @help.command()
    async def user(self, ctx):
        embed = discord.Embed(
            title="//help user",
            colour=discord.Colour.teal(),
            description="Infomations about user in the server")
        embed.add_field(
            name="Standard Commands List ",
            value= "`//user, `//info, `//userinfo` : Infomations about user: id, status, roles,...\n"
                   "`//avatar`: Fetch and display the requested users avatar.\n"
                   "etc: `//user` or `//user @Tantanyan#2303 `"
                    )
        await ctx.send(embed=embed)

    @help.command()
    async def pso2(self, ctx):
        embed = discord.Embed(
            title="//help pso2",
            colour=discord.Colour.teal(),
            description="Phantasy Star Online 2 ")
        embed.set_thumbnail(url="http://ww3.sinaimg.cn/crop.0.0.600.337.1000.562/4e4baa2egw1f6i46t0n7oj20go0a940q.jpg")
        embed.add_field(
            name="Standard Commands List ",
            value= "`//pso2`: Link Related to PSO: bumped, swiki,..\n"
                   )
        await ctx.send(embed=embed)

    @help.command()
    async def meme(self, ctx):
        embed = discord.Embed(
            title="//help meme",
            colour=discord.Colour.teal(),
            description="")
        embed.add_field(
            name="Meme list",
            value="`//bad`: \n"
                  "`//fack`: \n"
                  "`//haha`: Lol \n"
                  "`//smug`: \n"
                  "`//teehee`: \n"
                  "`//waa`,`//cry`: Wanna cry?\n"
                  "`//wat`,`//nani`,`//wut`: Nani the facka? \n"
                  "`//police`,`//mp`: Hello onii-chan, FBI waiting for you \n"
                  "`//salt`: Want some salt?\n"
                  "`//lenny` : ( ͡° ͜ʖ ͡°)\n"
        )
        await ctx.send(embed=embed)

    @help.command()
    async def server(self, ctx):
        embed = discord.Embed(
            title="//help server",
            colour=discord.Colour.teal(),
            description="")
        embed.add_field(
            name="List commands:",
            value="`//server`: about server\n"
                  "`//servericon`: server's icon\n"
        )
        await ctx.send(embed=embed)

    @help.command()
    async def other(self, ctx):
        embed = discord.Embed(
            title="//help other",
            colour=discord.Colour.teal(),
            description="")
        embed.add_field(
            name="Some stupid things",
            value="`//textflip`: Flipping some text, applies only to letters in alphabet (A-Z, a-z) and numbers (0-9)- eg: //textflip 3ktan-chan\n"
                  "`//poke`: poke bot ~~(but be carefull)~~ \n"
                  "`//countdown`: eg: //countdown 5 \n"
                  "`//ping`: pong\n"
                  "`//utb` or `//youtube`: seach on youtube - eg: //utb pso2 3ktan\n"
                  "`//feedback content`: Gives feedback about the bot - eg: //feedback I found some bugs, and this is a resuilt: <https://i.imgur.com/aS2CPTX.png> \n"
                  "`//donate`: Thank you for all your support~\n"
        )
        await ctx.send(embed=embed)

    @help.command()
    async def translate(self, ctx):
        embed = discord.Embed(
            title="//help translate",
            colour=discord.Colour.teal(),
            description="")
        embed.add_field(
            name="Translation",
            value="`//translate <language> <text>:` Translation to multiple languages - eg: `//translate japanese cute!!` \n"
                  "`//trans`: translation to english - eg: `//trans ありがとう` \n"
        )
        await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(Help_module(bot))
