import discord
from discord.ext import commands
from googlesearch import search

client = commands.Bot(command_prefix='!')

class GFinder(commands.Cog):
    def __init__(self, client):
        self.client = client

    def do_search(self, q):
        res = search(q, num=4, stop=5, pause=2)
        return res

    @commands.Cog.listener()
    async def on_ready(self):
        print('Laptop finder ready')

    @commands.command()
    async def find(self, ctx, *queries):
        query = ' '.join(queries)
        got = do_search(query)
        for i in got:
            await ctx.send(i)


def setup(client):
    client.add_cog(GFinder(client))
