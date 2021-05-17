from discord.ext import commands
from googlesearch import search
import random


class GFinder(commands.Cog):
    def __init__(self, client):
        self.client = client

    def flipper(self):
        rest = random.random()
        return 'heads' if rest < 0.5 else 'tails'

    @commands.Cog.listener()
    async def on_ready(self):
        print('coin flipper ready')

    @client.command()
    async def flip(self, ctx, amt: int):
        for i in range(amt):
            await ctx.send(flipper())
