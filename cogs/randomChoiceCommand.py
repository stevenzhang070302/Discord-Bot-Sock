import discord
import random
from discord.ext import commands

class randomChoiceCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Random choice command is online')

    #Commands
    @commands.command(aliases=['randomchoice', 'choice', 'random'])
    async def randomChoice(self, ctx, a, b, c, d, e): 
        responses = [a, 
                    b,
                    c,
                    d,
                    e
                    ]
        await ctx.send(f"I have choosen '{random.choice(responses)}' based on random choice select.")

    @randomChoice.error
    async def randomChoice_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await(ctx.send('Please enter 5 choices. If there are less than 5 choices please enter rerolls as extra choices.'))

def setup(client):
    client.add_cog(randomChoiceCommand(client))