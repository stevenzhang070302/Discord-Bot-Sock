import discord
import random
from discord.ext import commands

class badCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Ready to delete.')

    #Commands
    @commands.command()
    async def bad(self, ctx): 
        if author.id == "271794437284298764":
            await ctx.channel.purge(2)

def setup(client):
    client.add_cog(badCommand(client))