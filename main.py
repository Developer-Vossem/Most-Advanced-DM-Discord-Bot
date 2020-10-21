'''Importing Modules Required for the Bot'''
import json
import time
import discord
from discord.ext import commands
import colored 
from colored import fg, attr

'''Defining Colors and the Variables used in the Bot'''
red = fg('red')
green = fg('green')
blue = fg('blue')
clear = attr('reset')

with open('./utilities/config.json') as variables:
    config = json.load(variables)
token = config["token"]
prefix = config["prefix"]
cooldown = config["cooldown"]

client = commands.Bot(command_prefix = prefix)
client.remove_command('help')

'''Hitting up the Terminal when Bot Loads up'''

@client.event
async def on_ready():
    print(green + "The bot is now ready and fully operational." + clear)
    print(blue  + f"DM Bot Commands : \n{prefix}dmuser : DMs a specific user.\n{prefix}dmrole : DMs a users with a specific role.\n{prefix}dmall  : DMs everyone." )
    print(green+ "--------------------------------------------------" + clear + red + "Logs" + clear + green + "--------------------------------------------------" + clear)

############################ Command Area ############################

######################################################################
#                   DM User Command                                  #
######################################################################
@client.command()
async def dmuser(ctx, member : discord.Member = None,*, message = None):
    
    if member == None:
        await ctx.send("You've to mention a person to send him/her the Message.")
    elif message == None:
        await ctx.send("Please add a message, it can't be blank.")
    
    elif message != None and member != None:
        try:
            await member.send(message)
            print(green + "Success :" + clear +  f" Message has been successfully delievered to {member} !")
        except:
            print(red +   "Error   :" +clear+f" Message was not delievered to {member} !")
######################################################################
#                   DM Role Command                                  #
######################################################################
@client.command()
async def dmrole(ctx, role : discord.Role = None,*, message = None):
    
    if role == None:
        await ctx.send("Please mention a role.")
    elif message == None:
        await ctx.send("Please add a message, it can't be blank.")

    elif message != None and role != None:
        members = ctx.guild.members
        for member in members:
            if role in member.roles:
                try:
                    await member.send(message)
                    print(green + "Success :" + clear +  f" Message has been successfully delievered to {member} !")
                    time.sleep(cooldown)
                except:
                    print(red +   "Error   :" +clear+f" Message was not delievered to {member} !")
            else:
                pass
######################################################################
#                   DM All  Command                                  #
######################################################################
@client.command()
async def dmall(ctx,*, message = None):
    
    if message == None:
        await ctx.send("Please add a message, it can't be blank.")

    elif message != None:
        members = ctx.guild.members
        for member in members:
            try:
                await member.send(message)
                print(green + "Success :" + clear +  f" Message has been successfully delievered to {member} !")
                time.sleep(cooldown)
            except:
                print(red +   "Error   :" +clear+f" Message was not delievered to {member} !")
########################################################################







client.run(token)