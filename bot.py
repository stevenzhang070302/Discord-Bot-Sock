import discord
import random
import os
from discord.ext import commands, tasks
from discord.utils import get
from itertools import cycle

client = commands.Bot(command_prefix = '/') #client is the instance of the bot
status = cycle(['Origami', 'AP Research', 'Valorant', 'with Himself'])

@client.event #function
async def on_ready():
    change_status.start()
    # await client.change_presence(status=discord.Status.online, activity=discord.Game('Origami'))
    print('Bot Sock is ready')

@tasks.loop(seconds=600)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid command used.')

@client.event
async def on_member_join(member): #events
    print(f'{member} has joined a server.')

@client.event
async def on_member_remove(member): #events
    print(f'{member} has left a server.')

@client.command() #command
async def ping(ctx): #type /ping the bot says Pong!
    await ctx.send(f'Latency: {round(client.latency * 1000)}ms')



@client.command()
@commands.has_permissions(administrator=True)
async def load(ctx, extension): #cogs
    client.load_extension(f'cogs.{extension}')
@load.error
async def load_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await(ctx.send('You do not have the permissions to execute this protocol.'))

@client.command()
@commands.has_permissions(administrator=True)
async def unload(ctx, extension): #cogs
    client.unload_extension(f'cogs.{extension}')
@unload.error
async def unload_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await(ctx.send('You do not have the permissions to execute this protocol.'))

@client.command()
@commands.has_permissions(administrator=True)
async def reload(ctx, extension): #cogs
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
@reload.error
async def reload_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await(ctx.send('You do not have the permissions to execute this protocol.'))




for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('') #my bot's special code 
#I deleted it so nobody can hack my bot
#if you are trying to replicate you have to get your own special code
#see discord developers portal for more info