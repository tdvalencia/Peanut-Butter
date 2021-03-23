import os, time, json, random, requests
import discord, wikipedia
from discord.ext import commands
import sauce, sponge

description = '''the hamburger has arrived. this is the main bot file.'''

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='#', description=description, intents=intents)

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

    guild = message.guild.name
    data = f'{int(time.time())} {message.channel} {message.author}: {message.content}'

    if message.author == bot.user:
        print(data)
        return
    else:
        print(data)
        if sauce.checkJson('guilds.json', guild):
            try:
                sponge.logMessages(message.guild.name, data)
                sponge.updateServer('guilds.json', message.author.name, guild)
            except Exception as e:
                print(e)
        else:
            sponge.guildBuildLog(message.guild.name, message.author.name)
        await bot.process_commands(message)

@bot.listen()
async def on_message(message):
    if message.author != bot.user:
        guild = message.guild.name
        parse = message.content.split(' ')
        containsBad = None
        uri = 'https://media.giphy.com/media/TKGMv1ukCJWwvYsXse/giphy.gif'

        for word in parse:
            if sauce.checkText('readText/bad-words.txt', word):
                containsBad = True

        if containsBad:
            sponge.updateServer('badword.json', message.author.name, guild)
            # await message.channel.send('this bitch bouta get smoked for saying a no-no word')
            # await message.channel.send(uri)

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

@bot.command()
async def wiki(ctx, query: str):
    try:

        if 'rand' in ctx.message.content:
            r = wikipedia.random(1)
            page = wikipedia.page(r)
            summary = wikipedia.summary(r, sentences=5)
        else:
            search = wikipedia.search(query, results=1)
            page = wikipedia.page(search[0])
            summary = wikipedia.summary(search[0], sentences=5)

        n = random.randrange(int(len(page.images)))    
        embed = discord.Embed(title=page.title, url=page.url, description=summary)
        embed.set_image(url=page.images[n])
        await ctx.send(embed=embed)
    except Exception as e:
        print(e)
        embed = discord.Embed(title='Error', description=str(e))
        await ctx.send(embed=embed)

bot.run(sauce.getToken())