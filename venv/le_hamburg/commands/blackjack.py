import json, discord, random
from discord.ext import commands

class Blackjack(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def deal():
        '''deals cards in blackjack'''
        for player in range(0, 2):
            print(player)
            

