import os, json, time
import sauce

'''this is the data handler with functions that directs flow to files'''

dataPath = os.path.dirname(__file__) + '/data/'
guildLogs = dataPath + '/guildLogs/'

def updateJson(file: str, user: str):
    with open(dataPath + file, 'r+', encoding='utf-8') as jsonFile:
        content = json.load(jsonFile)

        if sauce.checkJson(file, user):
            content[user] += 1
        else:
            content[user] = 1

        jsonFile.seek(0)
        json.dump(content, jsonFile, indent=4)
        jsonFile.truncate()

def updateServer(file:str, user:str, server: str):
    with open(dataPath + file, 'r+', encoding='utf-8') as jsonFile:
        content = json.load(jsonFile)

        if sauce.checkServer(file, user, server):
            content[server][user] += 1
        else:
            content[server][user] = 1

        jsonFile.seek(0)
        json.dump(content, jsonFile)
        jsonFile.truncate()

def logMessages(guildName: str, logs: str):
    with open(guildLogs + f'{guildName}.txt', 'a', encoding='utf-8') as f:
        f.write(logs + '\n')

def guildBuild(guildName: str):
    with open(guildLogs + f'{guildName}.txt', 'w', encoding='utf-8') as f:
        f.write(f'Start of {guildName}\'s chat logs \n')

    updateJson('guilds.json', guildName)