import random as r
from .card import Card
from .bot import Bot
import discord
from discord.ext import commands
import threading

class Blackjack(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
        self.active = False
        self.gameOver = False
        
    @commands.command()
    async def bjackhelp(self, ctx):
        ctx.send('uhhh just look it up. i still have to write a doc about it.')

    @commands.command()
    async def bjack(self, ctx):
        '''play blackjack against Peanut Butter'''

        await ctx.message.delete()

        if not self.active:
            self.active = True

            cards = []
            jack = Bot()

            self.deal(cards)
            jack.play()

            embed = discord.Embed(title='Blackjack', description=f'{cards}\n{self.total(cards)}\nbot first: {jack.cards[0]}')
            msg = await ctx.send(embed=embed)
            finalmsg = await ctx.send('welcome')

            emojis = {
                'hit': '👇',
                'stay': '🖐️',
                'restart': '🔄',
                'stop': '🛑'
            }

            for emoji in emojis.values():
                await msg.add_reaction(emoji)

            def check(reaction, user):
                self.reacted = reaction.emoji
                return user == ctx.author and str(reaction.emoji) in emojis.values()

            while True:
                try: 
                    reaction, user = await self.bot.wait_for('reaction_add', timeout=30.0, check=check)
                    await reaction.remove(user)
                except Exception as e:
                    cards = []
                    jack.cards = []
                    embed = discord.Embed(title='Oop', description='time ran out')
                    await msg.edit(embed=embed)
                    self.active = False
                    break
                else:
                    if str(self.reacted) == emojis['hit'] and not self.gameOver:
                        self.hit(cards)
                        embed = discord.Embed(title='Blackjack', description=f'{cards}\n{self.total(cards)}\nbot first: {jack.cards[0]}')
                        await msg.edit(embed=embed)

                    elif str(self.reacted) == emojis['stay']:
                        text = self.checkValue(self.total(cards), jack.total())
                        await finalmsg.edit(content=text)
                        cards = jack.cards = []
                        self.gameOver = True

                    elif str(self.reacted) == emojis['restart']:
                        cards, jack = self.restart(cards, jack)
                        embed = discord.Embed(title='Blackjack', description=f'{cards}\n{self.total(cards)}\nbot first: {jack.cards[0]}')
                        await msg.edit(embed=embed)

                    elif str(self.reacted) == emojis['stop']:
                        self.restart(cards, jack)
                        embed = discord.Embed(title='Blackjack', description='game ended')
                        await msg.edit(embed=embed)
                        self.active = False
                        break
        else:
            await ctx.send('a game is running')
        

    def restart(self, l:list, jack:Bot):
        l = []
        jack.cards = []
        jack.play()
        self.deal(l)
        self.gameOver = False
        return l, jack

    def deal(self, l:list):
        for x in range(0,2):
            c = Card(r.randrange(1,13))
            if c.name == 'ace' and self.total(l) <= 10:
                c.value = c.setValue('aceEl')
                l.append(c)
            else:
                l.append(c)

    def hit(self, l:list):
        c = Card(r.randrange(1,13))
        if c.name == 'ace' and self.total(l) <= 10:
            c.value = c.setValue('aceEl')
            l.append(c)
        else:
            l.append(c)

    def total(self, l:list):
        result = 0
        for card in l:
            result += card.value
        return result

    def checkValue(self, total:int, jack:int):
        botTotal = jack
        result = f' bot total: {botTotal}'

        if total <= 21 and botTotal <= 21:
            if total > botTotal:
                return f'you win.' + result
            elif total < botTotal:
                return f'you lose.' + result
            else:
                return f'tie.' + result
        elif total <= 21 and botTotal > 21:
            return f'you win.' + result
        elif total > 21 and botTotal <= 21:
            return f'you lose.' + result
        else:
            return f'tie.' + result

    def ace(self):
        pass
    
#TODO: Make ace dynamically change value depending on what happens