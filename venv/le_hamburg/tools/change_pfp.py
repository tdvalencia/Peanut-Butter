import discord

#############################################################################################################################
# USAGE:                                                                                                                    #
# 0. Make sure you have python 3.5 + installed and have discord.py installed (pip3 install discord)                         #
# 1. Download the python file                                                                                               #
# 2. Change the token variable to hold your bots token and the pfp variable to hold the path to your desired pfp            #
# 3. Run your file using `python3 path/to/file.py                                                                           #
# 3. That's it, you can keep the file or delete it again!                                                                   #
#############################################################################################################################

client = discord.Client()

token = ''
pfp_path = 'C:/Users/Tony/Downloads/pidgeon.jpg'

fp = open(pfp_path, 'rb')
pfp = fp.read()

@client.event
async def on_ready():
    await client.user.edit(avatar=pfp)
    
client.run(token)