from discord.ext import commands
import json

def load_info():
    with open('tantanyan/utils/info.json') as data_file:
        try:
            data = json.load(data_file)
            return data
        except:
            print("Can not find tantanyan/utils/info.json. Please check again")


