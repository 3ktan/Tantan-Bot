import discord
from discord.ext import commands
import random
from tantanyan.utils import config

class Meme:
    def __init__(self, bot):
        self.bot = bot
        self.links = {"bad": ("http://i.imgur.com/7Ny0ESJ.png",
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
                      "wat": ("http://i.imgur.com/xBeUEmh.jpg",
                              "http://i.imgur.com/QEyMXCw.jpg",
                              "http://i.imgur.com/cbNegmA.jpg",
                              "http://i.imgur.com/5KeAhpE.jpg",
                              "http://i.imgur.com/AfzgsTO.jpg",
                              "http://i.imgur.com/Zkn67Wx.png",
                              "http://i.imgur.com/9V1ztaP.jpg",
                              "http://i.imgur.com/6HuNiHj.jpg",
                              "http://i.imgur.com/ARdiefz.png",
                              "https://img.memecdn.com/anime-version-wat_o_2196743.jpg",
                              "http://i.imgur.com/UXbTMTt.jpg",
                              "https://i.imgur.com/DupP8WR.png",
                              "https://i.imgflip.com/1majz3.jpg",
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
                                "http://i.imgur.com/yNqtdVX.jpg",
                                "https://i.imgur.com/xAQw8pK.gif",
                                "http://i2.kym-cdn.com/photos/images/newsfeed/000/936/668/a3e.jpg",
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
                               ),
                      # "feel": ("https://media.giphy.com/media/fxAx4sHwCO21G/giphy.gif",
                      #
                      #      ),
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

    @commands.command()
    async def smug(self, ctx):
        await ctx.send(embed=random.choice(self.meme_smug))

    @commands.command()
    async def teehee(self, ctx):
        await ctx.send(embed=random.choice(self.meme_teehee))

    @commands.command()
    async def waa(self, ctx):
        await ctx.send(embed=random.choice(self.meme_waa))

    @commands.command()
    async def wat(self, ctx):
        await ctx.send(embed=random.choice(self.meme_wat))

    @commands.command()
    async def police(self, ctx):
        await ctx.send(embed=random.choice(self.meme_police))

    @commands.command()
    async def salt(self, ctx):
        await ctx.send(embed=random.choice(self.meme_salt))
def setup(bot):
    bot.add_cog(Meme(bot))
