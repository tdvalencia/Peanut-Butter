import os, time, json, random, requests, io
import discord, wikipedia
from discord.ext import commands
import sauce, sponge
from commands import badword, wikiSearch, kenobi, bee, brrt
from Blackjack import card
from Blackjack import blackjack
from Bank import bank

description = '''hamburgers are cool'''

intents = discord.Intents.default()
intents.members = True

dataPath = os.path.dirname(__file__) + '/data/'

bot = commands.Bot(
    command_prefix='#', 
    description=description, 
    intents=intents,
    help_command=commands.DefaultHelpCommand(no_category='Basic')
)

bot.add_cog(badword.Badword(bot, dataPath))
bot.add_cog(wikiSearch.WikiSearch(bot))
bot.add_cog(kenobi.Kenobi(bot))
bot.add_cog(bee.BeeMovie(bot, dataPath))
bot.add_cog(brrt.Brrt(bot, dataPath))
bot.add_cog(blackjack.Blackjack(bot))
bot.add_cog(bank.Bank(bot))

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    activity = discord.Game(name="hjonks")
    await bot.change_presence(status=discord.Status.online, activity=activity)

@bot.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send('Hello. My command prefix is `#`. Use `#help` for a list of commands.')
        break

@bot.event
async def on_message(message):
    '''collects info on who sends messages'''

    data = f'{int(time.time())} {message.channel} {message.author}: {message.content}'

    if message.author == bot.user:
        print(data)
        return
    else:
        print(data)
        guild = message.guild.name
        if sauce.checkJson('guilds.json', guild):
            try:
                sponge.logMessages(message.guild.name, data)
                sponge.updateServer('guilds.json', str(message.author), guild)
            except Exception as e:
                print(e)
        else:
            sponge.guildBuildLog(message.guild.name, message.author.name)
        await bot.process_commands(message)

@bot.command()
async def clear(ctx, number:int=10):
    '''clears messages'''
    await ctx.channel.purge(limit=number+1)

@bot.command()
async def cool(ctx, name: str):
    '''Decides if u cool'''

    num = random.randrange(3)

    try:
        await ctx.message.delete()

        if sauce.checkText('readText/cool.txt', name):
            switcher = {
                0: f'{name} is cool',
                1: f'{name} is swag',
                2: f'{name} is pog'
            }
            await ctx.send(switcher.get(num, 'error'))
        else:
            switcher = {
                0: f'{name} is not cool',
                1: f'{name} is not swag',
                2: f'{name} is unpoggie'
            }
            await ctx.send(switcher.get(num, 'error'))
    except Exception as e:
        print(e)

@bot.command()
async def test(ctx):
    await ctx.send('test')

    msg = await bot.wait_for('message')
    if msg.content.lower() == "y":
        await ctx.send("You said yes!")
    else:
        await ctx.send("You said no!")

# @bot.command()
# async def bjack(ctx):
#     user = ctx.author
    

bot.run(sauce.getToken())