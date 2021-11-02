import discord
from discord.ext import commands

client = commands.Bot(command_prefix="!")


class GTS(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('dumbass alert ready')

    @commands.command()
    async def googl(self, ctx):
        pic = discord.File(r"../assets/gts.gif")
        await ctx.send(file=pic)
        print("sent gif")

    @googl.error
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("no args needed")


def setup(client):
    client.add_cog(GTS(client))
