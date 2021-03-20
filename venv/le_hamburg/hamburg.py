import discord, random, os, io
from discord.ext import commands


description = '''Yes the Hamburger has arrived'''

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='#', description=description, intents=intents)

path = os.path.dirname(__file__) + '/'

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
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command()
async def cool(ctx, name: str):
    """Decides if u cool"""

    cool = False

    with open(path + 'cool.txt', 'r') as f:
        nameList = f.readline().split(',')

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
        memeber = ''

        for user in ctx.guild.members:
            if name == user.name:
                memeber = user
        
        try:
            await ctx.send('air strike in bound')
            for i in range(0, 1):
                await ctx.send(memeber.mention)
        except:
            await ctx.send('user not found')
    else:
        await ctx.send('ur not cool enough')

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send('{0.name} joined in {0.joined_at}'.format(member))

@bot.command()
async def admin(ctx):
    if ctx.message.author.guild_permissions.administrator:
        await ctx.send('you are admin')
    else:
        await ctx.send('you are not admin')

bot.run('ODAzNjc0NjE1NjM2Njg4OTE2.YBBOTw.TFlh5qyjBPjxRF33P2p-0wdG5WA')