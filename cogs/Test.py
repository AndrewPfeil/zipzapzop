import discord
from discord.ext import commands 

colloseum = 660178172670640129 # colloseum channel id

class Test(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    ## BOOT EVENT CALLBACK ##
    @commands.Cog.listener()
    async def on_ready(self):
        print('zipzapzop is ready.')
        # LOGIN ANNOUNCEMENT
        channel = self.client.get_channel(colloseum) 
        await channel.send('Zipzapzop is now online.')

    ## LATENCY CHECK ##
    @commands.command(aliases = ['ping', 'test'])
    async def latency(self, ctx):
        await ctx.send(f'Latency: {round(self.client.latency * 1000)}ms')

def setup(client):
    client.add_cog(Test(client))