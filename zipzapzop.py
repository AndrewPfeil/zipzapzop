import discord 
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

# import json
# census = {}

# import logging
# logging.basicConfig(level=logging.INFO)


## BOOT EVENT CALLBACK ##
@client.event
async def on_ready():
 	print('zipzapzop is ready')
 	# LOGIN ANNOUNCEMENT
 	channel = client.get_channel(660178172670640129) #colloseum only
 	await channel.send('Logged on')


## LATENCY CHECK ##
@client.command()
async def ping(ctx):
	await ctx.send(f'Latency: {round(client.latency * 1000)}ms')


## MESSAGE EVENT CALLBACK ##
# @client.event
# async def on_message(message):
# 	if message.author == client.user:
# 		return

	# if message.content.startswith('!enter'):
	# 	await message.channel.send('You have entered the Colloseum.')

	# if message.content.startswith('!gen_tourney'):
	# 	# ? admin only?
	# 	# ? future dev: autorun on datetime (15th?)
	# 	# ? Single channel?
	# 	for member in client.get_all_members():
	# 		print(member.name, member.id)
	# 	# gen_swiss(member)
	# 	await message.channel.send('Tournament auto generation is under development.')

	# if message.content.startswith('!fight'):
	# 	# find_opponents()
	# 	await message.channel.send('Opponent finding is not currently supported.')

	# if message.content.startswith('!report'):
	# 	# reporter = author-message.author()
	# 	# collect_match(reporter, opponent, result)
	# 	# confirm_match(opponent, opponent, result_check)
	# 	# 	update_leaderboard()
	# 	await message.channel.send('Tournament results logging is not currently supported.')

	# if message.content.startswith('!leaderboard'):
	# 	# restrict to only display in the leaderboard channel
	# 	# possibly set up to auto update on month end in addition to user prompt
	# 	# delete old leaderboard display 
	# 	await message.channel.send('Leaderboard viewing is not currently supported.')
	

	

## GENERATE A SWISS TOURNAMENT USING GUILD LEADERBOARD AND CHANNEL MEMBERS ##
# def gen_swiss(member):

# 	#leaderboard = {}
# 	#tourney = {}
	
# 	#leaderboard = load_json_to_dict('leaderboard.json', 'r')

# 	for member in client.get_all_members():
# 	#	?try channel.get_all_mambers
# 		print(member.name, member.id)
	#	if member.id in leaderboard:
	#		tourney.append(member.id, leaderboard{member.id}[rank])
	#	else
	#		tourney.append(member.id, 0) 
	#		leaderboard.append(member.id, 0)

	# sort tourney by rank
	# assign oppenents as 10 closest rank (5 above, 5 below for most members)
	# how to store this data? nested dictionaries?
	# json the tourney? 


## FIND THE ASSIGNED OPPONENTS OF THE ASKER FOR THE CURRENT TOURNEY
#def find_opponents():
	# asker = author-message.author()
	# read tourney.json and send opponents and match status to askers dm

## PROMPT A USER TO REPORT MATCH RESULTS ##
# def collect_match(reporter, opponent, result):
	#send_message(reporter, 'Please report win/loss and opponent')
	# implement reactions for win loss and opponent query
	# result = bool


## PROMPT THE USER'S OPPONENT TO CONFIRM THE MATCH RESULT ##
# def confirm_match(reporter, opponent, result_check):
	#send_message(opponent, 'Please report win/loss against reporter)
	# repeat reaction implementation from collect_match()
	#result_check = bool 
	# ?record result in tourney.json

	# if result != result_check:
	#	query_admin(final_result)
	#	winner = 
	#	loser = 
	# else 
	#	winner = 
	#	loser = 


## PROMPT AN ADMIN TO RESOLVE MATCH REPORT CONFLICT ##
#def query_admin(final_result):
	#send__message(hardcode genjak, 'Match result dispute detected, please choose result)
	# choose winner or neither via 3 reaction buttons?


## UPDATE LEADERBOARD WITH FINAL TOURNAMENT RESULTS ##
#def update_leaderboard(winner, participant):
	# leaderboard{winner}[rank] = leaderboard{winner}[rank] + 40
	# leaderboard{loser}[rank] = leaderboard{loser}[rank] + 10

	# with open('leaderboard.json', 'w') as outfile:
    #	json.dump(leaderboard, outfile, sort_keys = True, indent = 4,
    #       ensure_ascii = False)


## BOT TOKEN ##
client.run('')