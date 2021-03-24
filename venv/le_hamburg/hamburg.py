import os, time, json, random, requests, io
import discord, wikipedia
from discord.ext import commands
import sauce, sponge
from commands import greetings, badword, wikiSearch

description = '''the hamburger has arrived. this is the main bot file.'''

intents = discord.Intents.default()
intents.members = True

dataPath = os.path.dirname(__file__) + '/data/'

bot = commands.Bot(command_prefix='#', description=description, intents=intents)

bot.add_cog(greetings.Greetings(bot))
bot.add_cog(badword.Badword(bot, dataPath))
bot.add_cog(wikiSearch.WikiSearch(bot))

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    activity = discord.Game(name="hjonks")
    await bot.change_presence(status=discord.Status.online, activity=activity)

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
                sponge.updateServer('guilds.json', message.author.name, guild)
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
async def brrt(ctx, member: discord.Member, message:str='', dm:str=''):
    '''strikes target with mentions'''
    # target = sauce.checkList(ctx.guild.members, name)
    target = member

    print(target)

    switcher = {
        0: 'airstrike inbound',
        1: 'enemy ac-130 above',
        2: 'enemy bogey in airspace',
        3: 'this is not a drill',
        4: '*alarm noises*'
    }

    r = int(random.randrange(5))

    if sauce.checkText('readText/brrt.txt', ctx.author.name):
        if dm == '':
            try:
                await ctx.message.delete()
                if target != None:
                    await ctx.send(switcher[r])
                    time.sleep(3)
                    for i in range(0, 20):
                        await ctx.send(f'<@{target.id}> {message}')
                        time.sleep(1)
                else:
                    raise Exception
            except Exception as e:
                print(e)
                await ctx.send('target not found')
        else:
            try:
                await ctx.message.delete()
                if target != None:
                    await target.send(switcher[r])
                    time.sleep(5)
                    for i in range(0, 20):
                        await target.send(message)
                        time.sleep(1)
                    await ctx.author.send('Target hit')
                else:
                    raise Exception
            except Exception as e:
                print(e)
                await ctx.send('target not found')
    else:
        await ctx.send('ur kinda cringe')

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

bot.run(sauce.getToken())