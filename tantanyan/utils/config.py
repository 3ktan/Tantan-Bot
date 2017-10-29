from discord.ext import commands
import json

def load_info():
    try:
        with open('tantanyan/utils/token.json') as data_file:
            data = json.load(data_file)
            return data
    except:
        print("Can not find tantanyan/utils/token.json. Please check again")


