import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix='!')


class Flipper(commands.Cog):
    def __init__(self, client):
        self.client = client

    def flipper(self):
        rest = random.random()
        return 'HEADS' if rest < 0.5 else 'TAILS'

    @commands.Cog.listener()
    async def on_ready(self):
        print('coin flipper ready')

    @client.command()
    async def flip(self, ctx, amt: int = 1):
        for i in range(amt):
            await ctx.send(f'`{self.flipper()}`')

    @flip.error
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("**Syntax:** `-flip <number of flips>`")


def setup(client):
    client.add_cog(Flipper(client))
