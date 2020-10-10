import discord
import random
from discord.ext import commands

class loveCalculatorCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Love Calculator command is online')

    #Commands
    @commands.command(aliases=['love calculate', 'loveCalculate', 'lovecalculate', 'love calculator', 'lovecalculator']) #command
    async def loveCalculator(self, ctx, a, b):
        compatibility = random.randrange(101)
        str(compatibility)
        compatibleResponses = ['You two are very compatible. Now go have fun in bed or something.',
                                'You guys are very compatible. Consider dating or continuing a healthy relationship.',
                                'Very compatible. So, when is the wedding?',
                                'The compatibility rating is very high. Have you two considered dating?',
                                'Caution! High compatibility score.'
                                ]
        semiCompatibleResponses =  ['You two are somewhat compatible.',
                                    'You guys are compatible. Your compatibility could be higher.',
                                    'Somewhat compatible.',
                                    'The compatibility rating is medium. You two have a good chance at having a good relationship.',
                                    'Warning! Medium compatibility score.'
                                    ]
        notCompatibleResponses =  ['You two are not compatible. I have a better chance at landing heads on a coin than you two dating.',
                                    'You guys are not compatible. Better luck next time.',
                                    'Not compatible.',
                                    'The compatibility rating is low. You two do not have a good chance at love.',
                                    'Nothing to see here. Low compatibility score.'
                                  ]

        # print(compatibility)
        await ctx.send(f'{a} and {b} have a compatibility score of {compatibility}%.')
        if compatibility >= 75:
            await ctx.send(f'{random.choice(compatibleResponses)}')
        elif compatibility >= 50 and compatibility < 75:
            await ctx.send(f'{random.choice(semiCompatibleResponses)}')
        elif compatibility >= 0 and compatibility < 50:
            await ctx.send(f'{random.choice(notCompatibleResponses)}')

    @loveCalculator.error
    async def loveCalculator_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await(ctx.send('Please enter two names you want to check for love compatibility.'))

def setup(client):
    client.add_cog(loveCalculatorCommand(client))