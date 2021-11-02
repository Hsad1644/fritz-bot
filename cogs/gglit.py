import discord
from discord.ext import commands

client = commands.Bot(command_prefix="!")


class GTS(commands.cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('dumbass alert ready')

    @commands.command()
    async def googl(self, ctx):
        with open("../assets/gts.gif", 'rb') as f:
            pic = discord.file(f)
            await ctx.send(file=pic)


def setup(client):
    client.add_cog(GTS(client))
