#functions
'''
def mysum(x=1,y=1):
    print(x+y)

#mysum(y=13,x = 9)keyword
mysum(13,12)
'''
'''
def mysum(x,y):
    res = x+y
    return 0

ss = mysum(12,12)
print(ss)
'''
'''
f = 0
print(f)

def do():
    global f
    f= 5
    print(f)

do()
print(f)
'''
'''
a = lambda  x,y :x+y
print(a(12,12))
print(type(a))
'''

for k,l in enumerate('firas_alhinde',1) :
    print(f'{k} -> {l}')
