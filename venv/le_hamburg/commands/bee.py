import discord, json
from discord.ext import commands
from le_hamburg import sauce, sponge

class BeeMovie(commands.Cog):
    def __init__(self, bot, dataPath):
        self.bot = bot
        self.dataPath = dataPath

    @commands.Cog.listener()
    async def on_message(self, message):

        arr = []

        if message.author != self.bot.user:
            guild = message.guild.name
            parse = message.content.split(' ')
            containsBee = None

            for word in parse:
                with open(self.dataPath + 'readText/entireBee.txt', 'r', encoding='utf-8') as f:
                    fileList = f.read()

                if word in parse:
                    containsBee = True

            if containsBee:
                sponge.updateServer('beeMovie.json', str(message.author), guild, 1)
                # await message.channel.send('you are plagiarizing the bee movie')

    @commands.command()
    async def turnitin(self, ctx):
        '''returns the times a user have used words in Bee Movie'''

        await ctx.message.delete()

        server = ctx.guild.name
        user = ctx.message.author.name

        with open(self.dataPath + 'beeMovie.json', 'r', encoding='utf-8') as f:
            data = json.load(f)

        userData = data[server][user]
        try:
            await ctx.send(f'You have used word from the bee movie ' + str(userData) + ' times.')
        except Exception as e:
            await ctx.send(f'You have not used words from the bee movie yet.')

    