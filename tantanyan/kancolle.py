import os
import io
import discord
from discord.ext import commands
import json

class Ship:
    def __init__(self,
                 seiyuu=None,
                 artist=None,
                 implement_on=None,
                 all_forms =[],
                 quotes=[],
                 character=None,
                 notes=None,
                 trivia=None,
                 quests=None,
                 cg_art=[],
                 ):
        self.seiyuu = seiyuu,
        self.artist = artist,
        self.implement_on = implement_on,
        self.all_forms = all_forms,
        self.quotes = quotes,
        self.character = character,
        self.notes = notes,
        self.trivia = trivia,
        self.quests = quests,
        self.cg_art = cg_art,

    @classmethod
    def from_file(cls, name, file):
        data = json.load(file)
        new_ship = cls(data['all_forms']['name'], data['all_forms']['id'], data['all_forms']['class'])
        return new_ship

    def embed_form(self):
        embed = discord.Embed(
            title=self.all_forms["name"],
            colour=discord.Colour.green(),
            )
        embed.add_field(
            name=format(self.all_forms["name"]),
            value="ID: "+self.all_forms["id"] + "Class: "+self.all_forms["class"]
        )
        return embed



class Kancolle:
    def __init__(self, bot, **kwargs):
        self.bot = bot
        self.ship_library = []
        # with open("data/ship_list.txt","r", encoding='utf-8') as file:
        #     for i in file:
        #         with open("data/kancolle/ship/{i[:-1]}.json","r", encoding='utf-8') as file:
        #             new_ship = Ship.from_file(i, file)
        #             self.ship_library.append(new_ship)

        for i in os.listdir(f"data/kancolle/ship"):
            with open(f"data/kancolle/ship/{i}", encoding='utf-8') as file:
                new_chip = Ship.from_file(i[:-5], file)
                self.ship_library.append(new_ship)

    def search(self, name):
        result = []
        for ship in self.ship_library:
            check = True
            for word in name.split():
                if word.lower() not in ship.all_forms['name'].lower():
                    check = False
                    break
            if check:
                result.append(ship)
        if len(result) > 1:
            for ship in result:
                if name.lower() == ship.all_forms['name'].lower() :
                    result = [ship, ]
                    break
        return result

    @commands.command()
    async def ship(self, ctx, *, name: str):
        result = self.search(name)
        if not result:
            await ctx.send("Can't find "+format(name)+" in database.")
            return
        if len(result) > 1:
            await ctx.send("Do you mean:\n```\n{}\nc: cancel\n```".format(
                '\n'.join([str(index + 1) + ": " + c.all_forms['name'] for index, c in enumerate(result)])))
            msg = await self.bot.wait_for("message", check=lambda m: m.author == ctx.author)
            try:
                if int(msg.content) - 1 in range(len(result)):
                    ship = result[int(msg.content) - 1]
            except:
                return
        else:
            ship = result[0]
        await ctx.send(embed=ship.embed_form())

def setup(bot):
    bot.add_cog(Kancolle(bot))