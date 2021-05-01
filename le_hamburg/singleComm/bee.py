import discord, json
from discord.ext import commands
import sponge, sauce

class BeeMovie(commands.Cog):
    def __init__(self, bot, dataPath):
        self.bot = bot
        self.dataPath = dataPath

    @commands.Cog.listener()
    async def on_message(self, message):

        try:
            arr = []

            if message.author != self.bot.user:
                guild = message.guild.name
                parse = message.content.split(' ')
                containsBee = None

                for word in parse:
                    with open(self.dataPath + 'readText/entireBee.txt', 'r', encoding='utf-8') as f:
                        fileList = f.read()

                    if word in fileList:
                        arr.append(word)
                        containsBee = True

                if containsBee:
                    sponge.updateServer('beeMovie.json', str(message.author), guild, len(arr))
                    # await message.channel.send('you are plagiarizing the bee movie')
        except Exception as e:
            pass
            

    @commands.command()
    async def turnitin(self, ctx):
        '''returns the times a user have used words in Bee Movie'''

        await ctx.message.delete()

        server = ctx.guild.name
        user = str(ctx.message.author)

        with open(self.dataPath + 'beeMovie.json', 'r', encoding='utf-8') as f:
            data = json.load(f)

        userData = data[server][user]
        try:
            await ctx.send(f'You have used words from the bee movie ' + str(userData) + ' times.')
        except Exception as e:
            await ctx.send(f'You have not used words from the bee movie yet.')

    