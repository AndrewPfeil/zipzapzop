import discord
from discord.ext import commands 

import json

server_id = 433917666596487168 # Ja'Lea server id

class Leaderboard(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    ## DISPLAY LEADERBOARD ##
    @commands.command(brief='--> See the current leaderboard', aliases = ['leaderboard', 'xp'])
    async def view(self, ctx):
        server = self.client.get_guild(server_id)

        with open(f'{server}_leaderboard.json') as json_file:
            xp_dict = json.load(json_file)

        await ctx.author.send(xp_dict)

def setup(client):
    client.add_cog(Leaderboard(client))