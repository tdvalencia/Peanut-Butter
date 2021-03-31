
import discord, numpy
from discord.ext import commands
import sauce, sponge

class Bank(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.command()
    async def openAcc(self, ctx):
        user = ctx.author
        server = ctx.guild.name

        if not sauce.checkServer('bank.json', str(user), str(server)):
            sponge.updateServer('bank.json', str(user), str(server), num=200)

    @commands.command()
    async def checkAcc(self, ctx):         
        user = ctx.author
        sever = ctx.guild.name

        await ctx.send('under construction')

    def addMoney(self, user:str, server:str, amt:int):
        sponge.updateServer('bank.json', user, server, amt)

    def remMoney(self, user:str, server:str, amt:int):
        sponge.updateServer('bank.json', user, server, (amt * -1))