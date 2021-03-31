import os, json
import matplotlib.pyplot as plt
import discord
from discord.ext import commands
import sauce, sponge

class Badword(commands.Cog):

    def __init__(self, bot, dataPath):
        self.bot = bot
        self.dataPath = dataPath

    @commands.command()
    async def curseIndex(self, ctx):
        '''creates chart with server curse count'''

        await ctx.message.delete()
        self.graph(ctx.guild.name)
        await ctx.send(file=discord.File(self.dataPath + 'chart.png'))
        os.remove(self.dataPath + 'chart.png')

    @commands.Cog.listener()
    async def on_message(self, message):
        
        arr = []

        if message.author != self.bot.user:
            guild = message.guild.name
            parse = message.content.split(' ')
            containsBad = None
            uri = 'https://media.giphy.com/media/TKGMv1ukCJWwvYsXse/giphy.gif'

            for word in parse:
                if sauce.checkText('readText/bad-words.txt', word):
                    arr.append(word)
                    containsBad = True

            if containsBad:
                sponge.updateServer('badword.json', str(message.author), guild, len(arr))
                # await message.channel.send('this bitch bouta get smoked for saying a no-no word')
                # await message.channel.send(uri)

    def graph(self, server:str):
        height = []
        left = []

        with open(self.dataPath + 'badword.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        for names in data[server]:
            height.append(data[server][names])
        
        for keys in data[server].keys():
            left.append(keys)

        plt.xlabel('cursers')
        plt.ylabel('curses')
        plt.title('these mfs curse too much')

        plt.bar(left, height, width=0.5, color = ['#ff8b00', '#3399ff'])

        plt.xticks(rotation=90, fontsize=9)
        plt.tight_layout()

        plt.savefig(self.dataPath + 'chart.png')
        plt.close()

    def pieChart(self, server:str):
        
        stats = []
        total = 0

        with open(self.dataPath + 'badword.json', 'r', encoding='utf-8') as f:
            data = json.load(f)

        for names in data[server]:
            total += data[server][names]
        print(stats)
        print(total)

