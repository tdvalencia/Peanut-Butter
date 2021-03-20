import discord, time, os, io, json, asyncio
from discord.ext import commands

description = '''Yes the Hamburger has arrived'''

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='#', description=description, intents=intents)
token = ''

dataPath = os.path.dirname(__file__) + '\\data\\'
brrtUsed = 0

def getToken():
    global token
    with open(dataPath + 'token.txt', 'r') as f:
        token = f.readline()
    return token

async def collectInfo():
    await bot.wait_until_ready()
    global brrtUsed

    while not bot.is_closed():
        try:
            with open(dataPath + 'stats.txt', 'a') as f:
                f.write(f'Time: {int(time.time())} | Brrt Used: {brrtUsed}\n')
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
    cool = False

    if name == None:
        await ctx.send('Enter a string after the command. ex "#cool Tony"')

    with open(dataPath + 'cool.txt', 'r') as f:
        nameList = f.readline().replace(' ', '').split(',')
        print(nameList)

    for names in nameList:
        if name.lower() == names:
            cool = True
            
    if cool == True:
        await ctx.send('{} is cool'.format(name))
    else:
        await ctx.send('{} is not cool'.format(name))

@bot.command()
async def brrt(ctx, name: str):

    if ctx.message.author.guild_permissions.administrator:
        global brrtUsed
        memeber = ''

        for user in ctx.guild.members:
            if name == user.name:
                memeber = user
        
        try:
            await ctx.send('air strike in bound')
            for i in range(0, 20):
                await ctx.send(memeber.mention)
            brrtUsed += 1
        except:
            await ctx.send('user not found')
    else:
        await ctx.send('ur not cool enough')

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send('{0.name} joined in {0.joined_at}'.format(member))

bot.loop.create_task(collectInfo())
bot.run(getToken())