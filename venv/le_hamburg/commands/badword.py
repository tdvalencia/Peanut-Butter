import os, json
import matplotlib.pyplot as plt
import discord
from discord.ext import commands

class Badword(commands.Cog):

    def __init__(self, bot, dataPath):
        self.bot = bot
        self.dataPath = dataPath

    @commands.command()
    async def curseIndex(self, ctx):
        await ctx.message.delete()
        self.graph(ctx.guild.name)
        await ctx.send(file=discord.File(self.dataPath + 'chart.png'))

    def graph(self, server:str):
        height = []
        left = []

        with open(self.dataPath + 'badword.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        for names in data[server]:
            height.append(data[server][names])
        
        for keys in data[server].keys():
            left.append(keys)

        # naming the x-axis
        plt.xlabel('cursers')
        # naming the y-axis
        plt.ylabel('curses')
        # plot title
        plt.title('these mfs curse too much')

        plt.bar(left, height, width=0.5, color = ['#ff8b00', '#3399ff'])

        plt.xticks(rotation=20, fontsize=9)
        plt.tight_layout()

        plt.savefig(self.dataPath + 'chart.png')