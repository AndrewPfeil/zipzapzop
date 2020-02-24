## ATTENTION! 
## This functionality relies on the "Gladiator" role existing in the Server.
## The bot must have role management permissions.

import discord
import asyncio
import datetime
from discord.ext import tasks, commands 
from discord.ext.commands import has_permissions

import json

main_channel = 433917666596487171 # colloseum channel id
gladiator = 678719198616354834 # gladiator role id
server_id = 433917666596487168 # Ja'Lea server id

class Colloseum(commands.Cog):
    
    def __init__(self, client):
        self.client = client
        self.day_checker.start()


    ## Note: this will continue after cog refresh and stack the loop. Fix in future
    @tasks.loop(hours=24.0) # Daily loop
    async def day_checker(self):
        await self.client.wait_until_ready()

        now = datetime.datetime.now()
        channel = self.client.get_channel(main_channel) 

        if now.day == 1: # if first of month
            await self.start_tourney()
        elif now.day == 15:
            await channel.send(f'The {now.month}/{now.year} tournament has ended.')
        elif now.day < 15: 
            await channel.send(f'The monthly tournament is in progress.')
        else:




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
    async def start_tourney(self):
        channel = self.client.get_channel(main_channel) 
        server = self.client.get_guild(server_id)
        counter = 0
        gladiator_counter = 0
        random = 0
        tourney_dict = {} 

        with open(f'{server}_leaderboard.json') as json_file:
            xp_dict = json.load(json_file)

        #await channel.send(xp_dict)

        role = discord.utils.get(server.roles, name='Gladiator')
        #role = discord.Guild.get_role(self,role_id = gladiator)

        for member in self.client.get_all_members():
            counter = counter + 1
            if role in member.roles: 
                #rank = randint(0,100) 
                # replace rank with xp ... xp_dict[member.id][xp]
                if f'{member.id}' in xp_dict:
                    tourney_dict[member.name] = {'id' : member.id, 'rank' : xp_dict[f'{member.id}']['xp']}
                else:
                    tourney_dict[member.name] = {'id' : member.id, 'rank' : 0}
                # print(member.name, member.id)
                await member.send("You have been entered into this month's Ja'Lea tournament!\n\nTo withdraw from monthly tournaments, type \".withdraw\" in the main chat.\n\nPlease report your wins by sending a direct message to Genjak.")
                gladiator_counter = gladiator_counter +1

        ranked_list = sorted(tourney_dict, key=lambda x: tourney_dict[x]['rank'])
        await channel.send(f'{gladiator_counter}/{counter} members in Ja\'Lea have been entered into this month\'s tournament')


        with open(f'{server.name}_tourney.json', 'w') as outfile:
            json.dump(tourney_dict, outfile)
        

    ## CHECK TOURNAMENT OPPONENTS ##
    @commands.command(brief='--> Check tournament opponents')
    async def rivals(self,ctx):
        server = self.client.get_guild(server_id)

        with open(f'{server}_tourney.json') as json_file:
            tourney_dict = json.load(json_file)

        ranked_list = []
        ranked_list = sorted(tourney_dict, key=lambda x: tourney_dict[x]['rank'])
        await ctx.send(ranked_list)

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
