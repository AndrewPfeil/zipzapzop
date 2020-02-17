## ATTENTION! 
## This functionality relies on the "Gladiator" role existing in the Server.
## The bot must have role management permissions.

import discord
from discord.ext import commands 
from discord.ext.commands import has_permissions

from random import randint
import json

class Colloseum(commands.Cog):
    
    def __init__(self, client):
        self.client = client


    ## TOURNAMENT SELF REGISTRATION ##  
    @commands.command(brief='--> Sign-up for monthly tourneys', aliases = ['join', 'enter', 'fight'])
    async def signup(self, ctx):
        member = ctx.author
        role = discord.utils.get(ctx.guild.roles, name='Gladiator')
        await member.add_roles(role)
        await ctx.send(f'{member} is now a {role} and will be entered into the next monthly tournament.')
        
    @commands.command(brief='--> Withdraw from monthly tourneys', aliases = ['leave', 'dropout', 'exit'])
    async def withdraw(self, ctx):
        member = ctx.author
        role = discord.utils.get(ctx.guild.roles, name='Gladiator')
        await member.remove_roles(role)
        await ctx.send(f'{member} has withdrawn from monthly tournaments.')


    ## SCHEDULE TOURNAMENT AND SAVE TO JSON ## 
    @commands.command(brief='--> Schedules tournament', hidden=True)
    @has_permissions(administrator=True)
    async def tourney(self,ctx):
        counter = 0
        gladiator_counter = 0
        random = 0
        tourney_dict = {} 

        role = discord.utils.get(ctx.guild.roles, name='Gladiator')

        for member in self.client.get_all_members():
            counter = counter + 1
            if role in member.roles: 
                rank = randint(0,100)
                tourney_dict[member.name] = {'id' : member.id, 'rank' : rank}
                # print(member.name, member.id)
                gladiator_counter = gladiator_counter +1

        print(tourney_dict)

        ranked_list = sorted(tourney_dict, key=lambda x: tourney_dict[x]['rank'])
        #await ctx.author.send('👋')
        await ctx.send(f'{gladiator_counter}/{counter} members in Ja\'Lea have been entered into this month\'s tournament')
        await ctx.send(ranked_list)
        #await ctx.send(f'{tourney_dict}')

        with open('tourney.json', 'w') as outfile:
            json.dump(tourney_dict, outfile)
        

    ## CHECK TOURNAMENT OPPONENTS ##
    @commands.command(brief='--> Check tournament opponents')
    async def rivals(self,ctx):

        with open('tourney.json') as json_file:
            tourney_dict = json.load(json_file)

        ranked_list = []
        ranked_list = sorted(tourney_dict, key=lambda x: tourney_dict[x]['rank'])

        member = ctx.author
        for i in range(len(ranked_list)):
            if ranked_list[i] == member.name: 
                rank = i

        if rank >= 2 and rank <= (len(ranked_list) - 3):
            await ctx.send(f'Your tough rivals are:\n-->{ranked_list[rank+2]}\n-->{ranked_list[rank+1]}')
            await ctx.send(f'Your easy rivals are:\n-->{ranked_list[rank-1]}\n-->{ranked_list[rank-2]}')
        elif rank == 1:
            await ctx.send(f'Your tough rivals are:\n-->{ranked_list[rank+2]}\n-->{ranked_list[rank+1]}')
            await ctx.send(f'Your easy rivals are:\n-->{ranked_list[rank-1]}')
        elif rank == 0:
            await ctx.send(f'Your tough rivals are:\n-->{ranked_list[rank+2]}\n-->{ranked_list[rank+1]}')
            await ctx.send('You don\'t have any easy rivals.')
        elif rank == len(ranked_list) - 2:
            await ctx.send(f'Your tough rivals are:\n-->{ranked_list[rank+1]}')
            await ctx.send(f'Your easy rivals are:\n-->{ranked_list[rank-1]}\n-->{ranked_list[rank-2]}')
        elif rank == len(ranked_list)-1:
            await ctx.send('You don\'t have any tough rivals.')
            await ctx.send(f'Your easy rivals are:\n-->{ranked_list[rank-1]}\n-->{ranked_list[rank-2]}')
        else:
            await ctx.send('Mistakes were made.')
            return

        await ctx.send('\nYou must choose the ruleset when battling your tough rivals.')

        

        

def setup(client):
    client.add_cog(Colloseum(client))