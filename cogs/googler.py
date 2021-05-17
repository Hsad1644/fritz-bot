import discord
from discord.ext import commands
from googlesearch import search


class GFinder(commands.Cog):
    def __init__(self, client):
        self.client = client

    def do_search(self, q):
        res = search(q, num=4, stop=5, pause=2)
        return res

    @commands.Cog.listener()
    async def on_ready(self):
        print('Laptop finder ready')

    @client.command()
    async def find(self, ctx, *queries):
        query = ' '.join(queries)
        got = do_search(query)
        for i in got:
            await ctx.send(i)
