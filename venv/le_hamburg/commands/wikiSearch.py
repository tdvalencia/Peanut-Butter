import discord, random, wikipedia
from discord.ext import commands

class WikiSearch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def wiki(self, ctx, query: str):
        '''a janky way of searching wikipedia. not too reliable'''
        try:
            if 'rand' in ctx.message.content:
                r = wikipedia.random(1)
                page = wikipedia.page(r)
                summary = wikipedia.summary(r, sentences=5)
            else:
                search = wikipedia.search(query, results=1)
                page = wikipedia.page(search[0])
                summary = wikipedia.summary(search[0], sentences=5)

            n = random.randrange(int(len(page.images)))    
            embed = discord.Embed(title=page.title, url=page.url, description=summary)
            embed.set_image(url=page.images[n])
            await ctx.send(embed=embed)
        except Exception as e:
            print(e)
            embed = discord.Embed(title='Error', description=str(e))
            await ctx.send(embed=embed)