import discord, os, time, json, random, wikipedia
from discord.ext import commands
import sauce, sponge

description = '''the hamburger has arrived. this is the main bot file.'''

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='#', description=description, intents=intents)

dataPath = os.path.dirname(__file__) + '\\data\\'

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

    if message.embeds:
        return
    else:
        guild = message.guild.name
        if sauce.checkJson('guilds.json', guild):
            data = f'{int(time.time())} {message.channel} {message.author}: {message.content}'
            try:
                sponge.logMessages(message.guild.name, data)
                sponge.updateServer('guilds.json', message.author.name, guild)
            except Exception as e:
                print(e)
            print(data)
        else:
            sponge.guildBuild(message.guild.name, message.author.name)
        await bot.process_commands(message)

@bot.command()
async def clear(ctx, number:int=10):
    '''clears messages'''
    await ctx.channel.purge(limit=number+1)

@bot.command()
async def brrt(ctx, name: str, message:str=''):
    '''strikes target with mentions'''
    target = sauce.checkList(ctx.guild.members, name)

    switcher = {
        1: 'airstrike',
        2: 'enemy ac-130 above',
        3: 'enemy bogey in airspace',
        4: 'this is not a drill',
        5: '*alarm noises*'
    }

    r = int(random.randrange(5))

    if sauce.checkText('readText/brrt.txt', ctx.author.name):
        try:
            await ctx.message.delete()
            if target != None:
                await ctx.send(switcher[r])
                time.sleep(3)
                for i in range(0, 20):
                    await ctx.send(f'{target.mention} {message}')
                    time.sleep(1)
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
                1: f'{name} is cool',
                2: f'{name} is swag',
                3: f'{name} is pog'
            }
            await ctx.send(switcher.get(num, 'error'))
        else:
            switcher = {
                1: f'{name} is not cool',
                2: f'{name} is not swag',
                3: f'{name} is unpoggie'
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