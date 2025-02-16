import  random

with open('sowpods.txt','r') as f:
    line  = f.read().splitlines()

    print(random.choices(line))