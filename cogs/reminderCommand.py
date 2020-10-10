import discord
import random
import datetime
import time
import asyncio
from discord.ext import commands

class reminderCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Reminder command is online')

    #Commands
    @commands.command(aliases=['remindme'])
    async def remind(self, ctx, a , b, *, member: discord.Member): 
        time = int(b) * 60
        # print(time)
        # print(a)
        # print(b)
        await ctx.send(f"Ok I will remind {member.mention} in {str(b)} minute(s) for scheduled activity/event '{a}'.")
        await asyncio.sleep(time)
        await ctx.send(f"Someone asked me to remind {member.mention} about the scheduled activity/event '{a}'.")

    @remind.error
    async def remindCommand_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await(ctx.send('Please enter the activity followed by the time in minutes you wanted to be reminded of the activity followed by the person you want to receive the reminder.'))
        elif isinstance(error, commands.UserInputError):
            await(ctx.send('Please enter the details in this format: /command activity time(in minutes) name(Discord name)'))

def setup(client):
    client.add_cog(reminderCommand(client))