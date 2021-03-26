import discord
from discord.ext import commands

class Kenobi(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        if 'hello there' in message.content.lower():
            e = discord.Embed(title='general kenobi')
            e.set_image(url='https://static.wikia.nocookie.net/star-wars-memes/images/f/fe/General_Kenobi%21.jpg/revision/latest/scale-to-width-down/340?cb=20200402023149')
            await message.channel.send(embed=e)

    