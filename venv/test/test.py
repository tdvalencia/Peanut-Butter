import os, io

path = os.path.dirname(__file__) + '/'

with open(path + 'cool.txt', 'r') as f:
    names = f.readline().split(',')
