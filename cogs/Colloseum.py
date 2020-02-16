## ATTENTION! 
## This functionality relies on the "Gladiator" role existing in the Server.
## The bot must have role management permissions.

import discord
from discord.ext import commands 


class Colloseum(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    @commands.command(brief='Sign-up for monthly tourneys', aliases = ['join', 'enter', 'fight'])
    async def signup(self, ctx):
        member = ctx.author
        role = discord.utils.get(ctx.guild.roles, name='Gladiator')
        await member.add_roles(role)
        await ctx.send(f'{member} is now a {role} and will be entered into the next monthly tournament.')
        

    @commands.command(brief='Withdraw from monthly tourneys', aliases = ['leave', 'dropout', 'exit'])
    async def withdraw(self, ctx):
        member = ctx.author
        role = discord.utils.get(ctx.guild.roles, name='Gladiator')
        await member.remove_roles(role)
        await ctx.send(f'{member} has withdrawn from monthly tournaments.')

def setup(client):
    client.add_cog(Colloseum(client))