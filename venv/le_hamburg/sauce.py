import json, os

'''this contains helpful functions for the bot and data handler to read and parse information'''

dataPath = os.path.dirname(__file__) + '\\data\\'

def checkJson(file: str, query: str):
    with open(dataPath + file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for q in data.keys():
        if query == q:
            return True
    return False

def checkServer(file: str, query: str, server: str):
    with open(dataPath + file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for q in data.keys():
        if server == q:
            for w in data[server].keys():
                if query == w:
                    return True
    return False

def checkText(file: str, query: str):
    with open(dataPath + file, 'r', encoding='utf-8') as f:
        fileList = f.readline().replace(' ', '').split(',')

    for q in fileList:
        if query.lower() == q:
            return True
    return False

def checkList(qlist: list, query: str):
    for q in qlist:
        if query == q.name:
            return q
    return None

def getToken():
    with open(dataPath + 'readText/token.txt', 'r', encoding='utf-8') as f:
        token = f.readline()
    return token