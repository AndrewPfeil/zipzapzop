# zipzapzop
Discord bot for tournament management

To run bot server: 

$ python3 zipzapzop.py

For discord api documentation see:
https://discordpy.readthedocs.io/en/latest/

Dev plan:

*UX*
-member joins server

Tournaments:
-sends "!joinswoshi", etc in main chat
-swoshi channel will become unlocked
-on tourney startdate, member will receive pm with rivals and match report instructions
-member commands:
    !leaveswoshi
        -member is removed from swoshi channel
    !result
        -member recieved pm with results survey
        -member selects win or loss and opponent
        -delay while opponent confirms (1day max)
        -member receives link to #tourney channel 
            -channel displays all match results
    !rank
        -member receives pm with xp, server currency, rank/role etc


*Application layer*
    -xp and currency depletion during tourney and chat inactivity
    -currency raise per activity in intervals (one point per 15 mins if active etc)

Tournaments:
    -sort particapants by xp
    -assign matches with nearest 10 ranked participants
    -notify participants 
    -underdog chooses match ruleset
    -match win by underdog = +40xp
    -match win by defender = +20xp
    -match loss = +10xp
    -tourney champion(s) split 100xp if tie


*Backend*
Functions:
    direct_msg(recipient, interaction, response)
        - input recipient and interaction type
        - conditional dialogue per interaction
            - some interactions return response
            - some conditions print full or partial db
  
    update_db(db_id, change_dict)
        - input the database to be updated
        - input member & change value
        - import db from .json into dict
        - parse for key and update value
        - resort
        - repost leaderboard or tourney

    Gen_tourney(channelid, type)
         -called on specified datetime
         -use channel id to
             - census of channel members
             - generate dictionary via leaderboard_db
         - sort participants_dict by rank
         - create matchups_dict using tournament type
             - seed matches using rank
             - initialise result to none (datatype?)
         - export db of match standings using

Databases:
    Leaderboard_db.json
         member.id, member{}
             "Name", member.name
             "Xp", xp val
             "Currency", currency val

    Swoshi_db.json
         Match, rivals{}
             "Underdog", member.id
             "Defender", member.id
             "Winner", member.id
        
            