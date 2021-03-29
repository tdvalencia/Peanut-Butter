import discord, random, time
from discord.ext import commands
from le_hamburg import sponge, sauce

class Brrt(commands.Cog):
    def __init__(self, bot, dataPath):
        self.bot = bot
        self.dataPath = dataPath

    @commands.command() #target: discord.Member, message:str='', dm:str='', num:int=5
    async def brrt(self, ctx, target: discord.Member, *args):
        '''strike a target with notifications'''

        num = 5 
        message = ''
        dm = False

        for arg in args:
            try:
                if type(int(arg)) == int:
                    num = int(arg)
            except Exception as e:
                if type(arg) == str and arg == 'dm':
                    dm = True
                elif type(arg) == str:
                    message = arg

        print(f'{target} {num} {message} {dm}')

        inbound = {
            0: 'airstrike inbound',
            1: 'enemy ac-130 above',
            2: 'enemy bogey in the airspace',
            3: 'this is not a drill',
            4: '*alarm noises*'
        }

        confirm = {
            0: 'good effect on target',
            1: 'direct hit',
            2: 'neutralized',
            3: 'target no longer exists',
            4: 'confirmed. strike was successful'
        }

        if sauce.checkText('readText/brrt.txt', ctx.author.name):
            if not dm:
                try:
                    await ctx.message.delete()
                    if target != None:
                        await ctx.author.send('standby')
                        await ctx.send(inbound[random.randrange(5)])
                        time.sleep(3)
                        for i in range(0, num):
                            await ctx.send(f'{target.mention} {message}')
                            time.sleep(1)
                    else:
                        raise Exception
                except Exception as e:
                    print(e)
                    await ctx.send('target not found')
            else:
                try:
                    await ctx.message.delete()
                    if target != None:
                        await ctx.author.send('standby')
                        await target.send(inbound[random.randrange(5)])
                        time.sleep(5)
                        for i in range(0, num):
                            await target.send(message)
                            time.sleep(1)
                        await ctx.author.send(confirm[random.randrange(5)])
                    else:
                        raise Exception
                except Exception as e:
                    print(e)
                    await ctx.send('target not found')
        else:
            await ctx.send('no')