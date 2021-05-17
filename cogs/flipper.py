import discord
from discord.ext import commands
import random


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
            await ctx.send(f'`{flipper()}`')


def setup(client):
    client.add_cog(Flipper(client))
