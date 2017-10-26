import discord
import aiohttp
from discord.ext import commands
from bs4 import BeautifulSoup

class Translate:
    '''
    Translation to multiple languages
    '''

    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession(loop=self.bot.loop, headers={"User-Agent": "AppuSelfBot"})

    # translation to multiple languages
    @commands.command(pass_context=True)
    async def translate(self, ctx, to_language, *, msg):
        async with self.session.get(
                "https://gist.githubusercontent.com/astronautlevel2/93a19379bd52b351dbc6eef269efa0bc/raw/18d55123bc85e2ef8f54e09007489ceff9b3ba51/langs.json") as resp:
            lang_codes = await resp.json(content_type='text/plain')
        real_language = False
        to_language = to_language.lower()
        for entry in lang_codes:
            if to_language in lang_codes[entry]["name"].replace(";", "").replace(",", "").lower().split():
                language = lang_codes[entry]["name"].replace(";", "").replace(",", "").split()[0]
                to_language = entry
                real_language = True
        if real_language:
            async with self.session.get("https://translate.google.com/m",
                                        params={"hl": to_language, "sl": "auto", "q": msg}) as resp:
                translate = await resp.text()
            result = str(translate).split('class="t0">')[1].split("</div>")[0]
            result = BeautifulSoup(result, "html.parser").text
            embed = discord.Embed(color=discord.Color.green())
            embed.add_field(name="Original", value=msg, inline=False)
            embed.add_field(name=language, value=result.replace("&amp;", "&"), inline=False)
            if result == msg:
                embed.add_field(name="Warning", value="This language may not be supported by Google Translate.")
            await ctx.message.delete()
            await ctx.send("", embed=embed)
        else:
            await ctx.send("`" + to_language + "` is not a real language.")

    # translation to english
    @commands.command(pass_context=True)
    async def trans(self, ctx, *, msg):
        await ctx.message.delete()
        async with self.session.get("https://translate.google.com/m",
                                    params={"hl": "english", "sl": "auto", "q": msg}) as resp:
            translate = await resp.text()
        result = str(translate).split('class="t0">')[1].split("</div>")[0]
        result = BeautifulSoup(result, "html.parser").text
        embed = discord.Embed(color=discord.Color.green())
        embed.add_field(name="Original", value=msg, inline=False)
        embed.add_field(name="English", value=result.replace("&amp;", "&"), inline=False)
        await ctx.send("", embed=embed)


def setup(bot):
    bot.add_cog(Translate(bot))