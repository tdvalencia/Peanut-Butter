import json

userDic = {'poop#1234': 0, 'l':0}

def dictionary(user: str):
    global userDic
    inside = False

    for key in userDic.keys():
        if key == user:
            inside = True

    if inside:
        userDic.update({user: userDic.get(user) + 5})
    else:
        userDic[user] = 1

print(userDic)

with open('test.json', 'w') as f:
    json.dump(userDic, f)