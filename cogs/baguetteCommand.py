import discord
import random
from discord.ext import commands

class baguetteCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Baguette command is online')

    #Commands
    @commands.command()
    async def baguette(self, ctx):
        responses = ['Je mange une pomme.', 
                    'Un deux trois quatre cinq six sept huit neuf dix.',
                    'William is a really spicy boi.',
                    'Soyboy.',
                    ':thinking:',
                    'Hmmmmmmmmm.',
                    'No taxation without representation.',
                    'The fanciest dog gets the shrimp.',
                    ':|',
                    'Ok buddy.',
                    'Ha simp.',
                    'Alexander Hamilton.',
                    'The smartest dog shoots the biggest gun.',
                    'Zoinks!',
                    'wdym',
                    'lets see you make it with graphics',
                    "ok you're not my buddy anymore",
                    'F',
                    'hahahahaha',
                    "lately my shower isn't getting as cold as i want it",
                    'Incredible, absolutely phenonmenal',
                    'bruh',
                    'ur mom broke a ladder',
                    'vr therapy is REAL',
                    'This is so sad',
                    'Im not flexing anything, im just calling you guys not smart.',
                    '?',
                    'yum yum in my tum tum',
                    "you're hmmm",
                    'hmmmmm',
                    'epic',
                    'no need to thank me',
                    'why are you so happy',
                    'smh you only record bad clips'
                    ]
        await ctx.send(random.choice(responses))

def setup(client):
    client.add_cog(baguetteCommand(client))
    