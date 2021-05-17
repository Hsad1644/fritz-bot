import discord
import random
from discord.ext import commands
import os
from googlesearch import search
import scraper
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")


def do_search(q):
    res = search(q, num=4, stop=5, pause=2)
    return res


def flipper():
    rest = random.random()
    return 'heads' if rest < 0.5 else 'tails'


client = commands.Bot(command_prefix='-')


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('Holden Tudiks'))
    print('bot is ready')


# @client.command(aliases=['pg'])
# async def ping(ctx):  # command name
#     await ctx.send('pong')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Syntax Error")


@client.command()
async def find(ctx, *queries):
    query = ' '.join(queries)
    got = do_search(query)
    for i in got:
        await ctx.send(i)


@client.command()
async def flip(ctx, amt: int):
    for i in range(amt):
        await ctx.send(flipper())


@client.command()
async def laptops(ctx, *q):
    qs = ' '.join(q)
    searchResults = scraper.finder(qs)

    out = discord.Embed(
        title='Search results',
        description='List of laptop resuslts',
        colour=discord.Colour.gold()
    )

    out.set_footer(text="That's all")
    out.set_thumbnail(
        url='https://cdn.imgbin.com/22/23/21/imgbin-united-states-pepe-the-frog-internet-meme-4chan-united-states-hmBcA5YpFcW3nUnxvrYmnkv0v.jpg')

    for i, j in zip(searchResults, range(0, len(searchResults))):
        out.add_field(name=f'Laptop {j+1}',
                      value=f"[click here]({'https://amazon.in/'+str(i['href'])})", inline=False)

    await ctx.send(embed=out)


@laptops.error
async def lapS_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Enter query values in `-laptop <values>`')


@flip.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("**Syntax:** `-flip <number of flips>`")


client.run(TOKEN)