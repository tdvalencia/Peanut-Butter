import discord
from discord.ext import commands
import random

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)

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
    #role = discord.utils.get(member.guild.roles, name='borger')

    await channel.send('The Hamburger welcomes you ' + member.mention)
    #await member.add_roles(role)

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
    print(name.lower())
    if name.lower() == 'tony' or name.lower() == 'hamburger' or name.lower() == 'hamburgers':
        await ctx.send('{} is cool'.format(name))
    else:
        await ctx.send('{} is not cool'.format(name))

#TODO: Try catch block ^^^^

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send('{0.name} joined in {0.joined_at}'.format(member))

bot.run('ODAzNjc0NjE1NjM2Njg4OTE2.YBBOTw.TFlh5qyjBPjxRF33P2p-0wdG5WA')