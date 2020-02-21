import discord
from discord.ext import commands 

main_channel = 433917666596487171 

class Test(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    ## BOOT EVENT CALLBACK ##
    @commands.Cog.listener()
    async def on_ready(self):
        print('zipzapzop is now online.')
        # LOGIN ANNOUNCEMENT
        channel = self.client.get_channel(main_channel) 
        await channel.send('zipzapzop is now online.')

    ## LATENCY CHECK ##
    @commands.command(brief='--> Check bot latency', aliases = ['ping', 'test'])
    async def latency(self, ctx):
        await ctx.send(f'Latency: {round(self.client.latency * 1000)}ms')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.client.get_channel(main_channel) 
        await channel.send(f"""Welcome to the server {member.mention}""")

def setup(client):
    client.add_cog(Test(client))