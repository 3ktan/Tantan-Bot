import discord
from discord.ext import commands
import random
from tantanyan.utils import config

class Meme:
    def __init__(self, bot):
        self.bot = bot
        self.links = {"bad": ("http://i.imgur.com/7Ny0ESJ.png",
                              "https://cdn.weeb.sh/images/ByIcZUPuZ.gif",
                              "https://cdn.weeb.sh/images/HkHFyIw_W.gif",
                              "https://i.imgur.com/IgGro8f.jpg",
                              "https://i.imgur.com/C4r251q.jpg",
                              "http://i.imgur.com/Z7dZfyl.jpg",
                              "http://i.imgur.com/NWbjLFL.gif",
                              "http://i.imgur.com/miuPFoR.jpg",
                              "http://i.imgur.com/z9V8maO.gif",
                              "http://i.imgur.com/2n8Ntpo.jpg",
                              "http://i.imgur.com/lL8PsVa.jpg",
                              "https://img4.hostingpics.net/pics/261404tumblrosktlcLFrl1qa94xto2500.gif",
                              "http://i.imgur.com/T8IAsHf.jpg",
                              "http://pa1.narvii.com/5768/f564759f8230e0843e746c26112844f7a44b64dc_hq.gif",
                              "http://images6.fanpop.com/image/answers/3115000/3115913_1356920797648.92res_400_298.jpg",
                              "http://pm1.narvii.com/6282/fdb0eadb51db4879525261374256bd3ab1aaaeca_hq.jpg",
                              "https://media.giphy.com/media/QlkiPtWYWRtgQ/source.gif",
                              "http://images6.fanpop.com/image/answers/3529000/3529553_1400944684950.47res_476_271.jpg",
                              "http://static.tvtropes.org/pmwiki/pub/images/critical_kick_4026.png",
                              "https://cdn.weeb.sh/images/HkZ6v0FOb.gif",
                              "https://i.imgur.com/LSjmc5f.jpg",
                              "https://i.imgur.com/6gSoKkn.jpg",
                              "https://i.imgur.com/Xykccyf.png",
                              "https://i.imgur.com/mLjtoQb.jpg",
                              "https://i.imgur.com/833wim4.png",
                              "https://i.imgur.com/oVnZtq6.jpg",
                              "https://i.imgur.com/wNsbcTC.jpg",
                              ),
                      "fack": ( "http://i.imgur.com/0yNkFvN.jpg",
                                "http://i.imgur.com/yoE4tuK.jpg",
                                "http://i.imgur.com/v8pWOz4.jpg",
                                "http://i.imgur.com/rcG5dn3.jpg",
                                "http://i.imgur.com/L9XYqwr.jpg",
                                "http://i.imgur.com/I5l0ZuM.jpg",
                                ),
                      "haha": ("http://i.imgur.com/k7ebYah.jpg",
                               "http://i.imgur.com/YTuvyme.gif",
                               "http://i.imgur.com/fP3GWOF.png",
                               "https://i.imgur.com/mAC8V9m.jpg",
                               "http://i.imgur.com/3YhGzGH.gif",
                               "http://i.imgur.com/UBXGPX4.jpg",
                               "http://i.imgur.com/SWQcgX2.jpg",
                               "http://i.imgur.com/cp88PU3.gif",
                               "http://i.imgur.com/P7qfcqr.gif",
                           ),
                      "smug": ("http://i.imgur.com/OftBCI6.png",
                               "http://i.imgur.com/SYdxXzU.png",
                               "http://i.imgur.com/sGCgKiq.jpg",
                               "http://i.imgur.com/LUhs2gw.jpg",
                               "http://i.imgur.com/tbuSF7n.jpg",
                               "http://i.imgur.com/kyphT97.jpg",
                               "http://i.imgur.com/PPVZTXY.gif",
                               "http://i.imgur.com/o1JvcB9.jpg",
                               "http://i.imgur.com/LPJbWkH.jpg",
                               "http://i.imgur.com/7AlFiQx.jpg",
                               "http://i.imgur.com/7xPHpHj.jpg",
                               "https://cdn.discordapp.com/attachments/280534991685812235/332414832290562048/19399668_954326081373656_8260916710232556651_n.jpg",
                               "http://i.imgur.com/20FlrNU.jpg",
                               "http://i.imgur.com/yQBGvCJ.jpg",
                               "http://i.imgur.com/6SIiocG.jpg",
                               "http://i.imgur.com/SJFPRSX.jpg",
                               "http://i.imgur.com/9UxAzjQ.jpg",
                               "http://i.imgur.com/pjvmtQE.jpg",
                               "http://i.imgur.com/UU8ddwX.gif",
                               "http://i.imgur.com/ggg9W2c.png",
                               "https://pbs.twimg.com/media/DHOTgo0UQAA1A7_.jpg",
                               "https://media.giphy.com/media/SCkrHJJE55js4/giphy.gif",
                               "http://pa1.narvii.com/5983/4ad906dd0a0438656d4516ab97f2017cdc5348c8_hq.gif",
                               "http://livedoor.blogimg.jp/niwakasokuhou/imgs/6/a/6a5a8b19.jpg",
                               "http://i0.kym-cdn.com/photos/images/newsfeed/000/928/011/832.jpg",
                               "http://i0.kym-cdn.com/photos/images/newsfeed/000/928/760/db8.gif",
                               "http://i0.kym-cdn.com/photos/images/newsfeed/000/928/974/dc8.png",
                               "http://i0.kym-cdn.com/photos/images/newsfeed/000/928/382/397.jpg",
                               "https://ih1.redbubble.net/image.361927158.3979/sticker,375x360-bg,ffffff.png",
                               "https://68.media.tumblr.com/3a1cc5f57ca5be82beebff7804d18275/tumblr_oiua2bpOZG1vje8zyo3_500.jpg",
                               "http://att.bbs.duowan.com/forum/201707/29/215848e33ychm6636kziv9.jpg",

                               ),
                      "teehee": ("http://i.imgur.com/GOkAKvV.png",
                                 "http://i.imgur.com/ecWHIm0.png",
                                 "http://i.imgur.com/flC4HpD.png",
                                 "http://ddn.i.ntere.st/p/11192319/image",
                                 "http://24.media.tumblr.com/d176debb19032ba19f45f99c6f8ed99e/tumblr_mm3i7k8MM71rz2r4lo2_500.png",
                                 "http://livedoor.blogimg.jp/ninelives69/imgs/8/d/8d5861ba-s.jpg",
                                 "http://blog-imgs-55.fc2.com/m/o/e/moerukabunushi/2012052622111960bs.jpg",
                                 "https://pbs.twimg.com/media/C5j7fdWUsAAZ-fz.jpg",
                                 "https://pbs.twimg.com/media/Bvz-vkrCIAAJK4R.jpg",
                                 "https://i.imgur.com/zYDTZgi.jpg",
                                 ),
                      "waa": ("http://i.imgur.com/LgLzolV.gif",
                              "http://i.imgur.com/81r4YWU.jpg",
                              "http://i.imgur.com/ED5tyUZ.gif",
							  "https://media.giphy.com/media/2i0SGzoxG2WWs/giphy.gif",
							  "https://pbs.twimg.com/media/C3gPvdFUoAAi7rY.jpg",
							  "https://media.giphy.com/media/4pk6ba2LUEMi4/giphy.gif",
                              "http://i.imgur.com/seQGtgT.gif",
                              "http://i0.kym-cdn.com/photos/images/newsfeed/000/871/687/a7c.gif",
                              "http://i0.kym-cdn.com/photos/images/original/001/230/774/9b2.gif",
                              "https://gifimage.net/wp-content/uploads/2017/07/anime-cry-gif-24.gif",
                              "https://gifimage.net/wp-content/uploads/2017/07/anime-cry-gif-16.gif",
                              "http://pm1.narvii.com/6480/2d3c203b551e9b9312325234ee09106d96d6bd8f_hq.jpg",
                              "https://i.imgur.com/4AKe8DH.jpg",
                              "https://i.imgur.com/MnynL18.jpg",
                              "https://i.imgur.com/bVz8yLp.jpg",
                              "https://i.imgur.com/ymvCT4A.jpg",
                              ),
                      "wat": ( "http://i.imgur.com/cbNegmA.jpg",
                              "http://i.imgur.com/AfzgsTO.jpg",
                              "http://i.imgur.com/Zkn67Wx.png",
                              "http://i.imgur.com/9V1ztaP.jpg",
                              "http://i.imgur.com/6HuNiHj.jpg",
                              "http://i.imgur.com/ARdiefz.png",
                              "https://i.imgur.com/DupP8WR.png",
                               "https://i.imgur.com/cj40D7x.jpg",
                               "https://i.imgur.com/hMq92mO.jpg",
                              ),
                      "wut": ("https://i.imgur.com/i97Qedz.jpg",
                              "https://i.imgur.com/HXxbMx2.jpg",
                              "https://i.imgur.com/9481pXn.jpg",
                              "https://i.imgur.com/lI6WGq6.jpg",
                              "https://i.imgur.com/iM6757u.jpg",
                              "https://i.imgur.com/BeRwU4o.jpg",
                              ),
                      "police": ("http://i.imgur.com/CYimeUd.jpg",
                                 "http://i3.kym-cdn.com/photos/images/newsfeed/001/176/546/a72.jpg",
                                "http://i.imgur.com/Jyzfm9o.jpg",
                                "http://i.imgur.com/mU7O3uX.png",
                                "http://i.imgur.com/9PPaV1i.jpg",
                                "http://i.imgur.com/GcKhkyq.png",
                                "http://i.imgur.com/g5EnTRo.jpg",
                                "http://i.imgur.com/bX15Mvp.jpg",
                                "http://i.imgur.com/RzBrjhc.gif",
                                "http://i.imgur.com/MND5tpg.jpg",
                                "http://i.imgur.com/A8Fmt4Z.png",
                                "http://i.imgur.com/seUOidB.jpg",
                                "http://i.imgur.com/bmjq17i.jpg",
                                "https://cdn.discordapp.com/attachments/270766856984461312/372957450925768704/22792153_10212876557001148_6732281705568977746_o.jpg",
                                "http://i.imgur.com/yNqtdVX.jpg",
                                "https://i.imgur.com/xAQw8pK.gif",
                                "http://i2.kym-cdn.com/photos/images/newsfeed/000/936/668/a3e.jpg",
                                 "https://i.imgur.com/uAfFojF.jpg",
                                 "https://i.imgur.com/VqiKQWr.jpg",
                                 "https://i.imgur.com/Ih0hMU9.png",
                                 "https://i.imgur.com/v0ugyB8.png",
                                 "https://i.imgur.com/l0hA8bo.jpg",
                                 "https://i.imgur.com/mR1zqYw.jpg",
                                 "https://i.imgur.com/Ms3WK7V.jpg",
                                 "https://i.imgur.com/JuBsz4O.gif",
                                 ),
                      "salt": ("http://i.imgur.com/lzfdjBi.jpg",
                               "http://i.imgur.com/c0tnUoR.jpg",
                               "http://i.imgur.com/9FK4ETL.jpg",
                               "http://i.imgur.com/ZgxJgZ7.png",
                               "http://i.imgur.com/uUUY8tN.jpg",
                               "http://i.imgur.com/6iqquJw.gif",
                               "http://i.imgur.com/j0yJDwq.jpg",
                               "http://i.imgur.com/Zy4IQde.jpg",
                               "https://i.pinimg.com/600x315/cd/8b/85/cd8b851e8db56c0aa3d0b3333f010ecf.jpg",
                               "https://i.imgur.com/jyH9p7I.png",
                               "https://i.pinimg.com/474x/59/4c/46/594c46cd5a97af5cc8a78353211120fb--chibi-characters-kawaii.jpg",
                               "https://farm3.static.flickr.com/2834/32026289914_9040816149_b.jpg",
                               "https://i.imgur.com/0qeD1JD.jpg",
                               ),
                      "suicide": ("https://i.imgur.com/bmOqRTP.jpg",
                                  "https://i.imgur.com/HmbFzRC.png",
                                  "https://i.imgur.com/NPMwY2e.jpg",
                                  "https://i.imgur.com/lKgGp8i.png",
                                 ),
                      "heartattack": ("https://i.imgur.com/aj5T5a2.jpg",
                                      "https://i.imgur.com/XyeMgaO.png",
                                      "https://i.imgur.com/jxgYd26.png",
                                      "https://i.imgur.com/LAsVXhK.jpg",
                                      "https://i.imgur.com/k3HGTRd.png",

                           ),
                      "justasplanned": ("https://i.imgur.com/Uw7jbUn.jpg",

                           ),
                      # "": ("",
                      #
                      #      ),
                      }
        for name, links in self.links.items():
            self.add_meme(name, links)

    def add_meme(self, name, links):
        setattr(self, "meme_" + name, [])
        for link in links:
            new_embed = discord.Embed()
            new_embed.set_image(url=link)
            getattr(self, "meme_" + name).append(new_embed)


    @commands.command()
    async def bad(self, ctx):
        await ctx.send(embed=random.choice(self.meme_bad))

    @commands.command()
    async def fack(self, ctx):
        await ctx.send(embed=random.choice(self.meme_fack))

    @commands.command()
    async def haha(self, ctx):
        await ctx.send(embed=random.choice(self.meme_haha))

    @commands.command(aliases=["( ͡° ͜ʖ ͡°)"])
    async def smug(self, ctx):
        await ctx.send(embed=random.choice(self.meme_smug))

    @commands.command()
    async def teehee(self, ctx):
        await ctx.send(embed=random.choice(self.meme_teehee))

    @commands.command(aliases=["cry"])
    async def waa(self, ctx):
        await ctx.send(embed=random.choice(self.meme_waa))

    @commands.command(aliases=["what",])
    async def wat(self, ctx):
        await ctx.send(embed=random.choice(self.meme_wat))

    @commands.command(aliases=["nani!"])
    async def wut(self, ctx):
        await ctx.send(embed=random.choice(self.meme_wut))

    @commands.command(aliases=["mp"])
    async def police(self, ctx):
        await ctx.send(embed=random.choice(self.meme_police))

    @commands.command()
    async def salt(self, ctx):
        await ctx.send(embed=random.choice(self.meme_salt))

    @commands.command()
    async def lenny(self, ctx):
        await ctx.send("( ͡° ͜ʖ ͡°)")

    @commands.command()
    async def suicide(self, ctx):
        await ctx.send(embed=random.choice(self.meme_suicide))

    @commands.command(aliases=["kidney","$"])
    async def money(self, ctx):
        embed = discord.Embed( )
        embed.set_image(url="https://i.imgur.com/4T1o44K.jpg")
        await ctx.send(embed=embed)

    @commands.command(aliases=["nosebleed","heartatk"])
    async def heartattack(self, ctx):
        await ctx.send(embed=random.choice(self.meme_heartattack))

    @commands.command()
    async def justasplanned(self, ctx):
        await ctx.send(embed=random.choice(self.meme_justasplanned))
def setup(bot):
    bot.add_cog(Meme(bot))
