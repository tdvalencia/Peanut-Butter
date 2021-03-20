import discord, time, os, io, json, asyncio
from discord.ext import commands

description = '''Yes the Hamburger has arrived'''

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='#', description=description, intents=intents)

dataPath = os.path.dirname(__file__) + '\\data\\'
brrtUsed = coolUsed = 0

def getData():
    global brrtUsed, coolUsed
    with open(dataPath + 'stats.json', 'r') as f:
        data = json.load(f)
        brrtUsed = data['brrt'][0]['timesUsed']
        coolUsed = data['cool'][0]['timesUsed']

def getToken():
    with open(dataPath + 'token.txt', 'r') as f:
        token = f.readline()
    return token

async def collectStats():
    await bot.wait_until_ready()
    global brrtUsed

    while not bot.is_closed():
        try:
            with open(dataPath + 'stats.json', 'r+') as jsonFile:
                data = json.load(jsonFile)

                data['brrt'][0]['timesUsed'] = brrtUsed
                data['cool'][0]['timesUsed'] = coolUsed

                jsonFile.seek(0) #Set cursor to beginning
                json.dump(data, jsonFile)
                jsonFile.truncate() #deals with case if new data is smaller than prev

            await asyncio.sleep(120)
        except Exception as e:
            print(e)
            await asyncio.sleep(120)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_member_join(member):
    print('New member joined.')
    channel = bot.get_channel(802197379146973214)
    await channel.send('The Hamburger welcomes you ' + member.mention)

@bot.command()
async def cool(ctx, name: str):
    """Decides if u cool"""
    global coolUsed
    cool = False

    with open(dataPath + 'cool.txt', 'r') as f:
        nameList = f.readline().replace(' ', '').split(',')

    for names in nameList:
        if name.lower() == names:
            cool = True
            
    if cool == True:
        await ctx.send('{} is cool'.format(name))
    else:
        await ctx.send('{} is not cool'.format(name))
    coolUsed += 1

@bot.command()
async def brrt(ctx, name: str):

    if ctx.message.author.guild_permissions.administrator:
        global brrtUsed
        member = None

        for user in ctx.guild.members:
            if name == user.name:
                member = user
        
        try:
            await ctx.message.delete()
            if member != None:
                await ctx.send('airstrike inbound')
                time.sleep(3)
                for i in range(0, 20):
                    await ctx.send(member.mention)
                brrtUsed += 1
            else:
                raise Exception
        except:
            await ctx.send('target not found')
    else:
        await ctx.send('u do not have airstrike capabilities')

@bot.command()
async def stats(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send('{0.name} joined in {0.joined_at}'.format(member))

getData()
bot.loop.create_task(collectStats())
bot.run(getToken())