

'''
def multi_application(start,end,s1,e1):
    for i in range(start,end+1):

        for j in range(s1,e1+1):
             print(f'{i} * {j} = {i * j}')
        print('-'*50)


multi_application(4,7,5,9)



'''
'''
user = input('enter the name\n')
u=[]
for name in user:
    if name not in u :
        u.append(name)
        

print(*u)
'''
"""
class Game:
    def __init__(self):
        while True:
            print('''Welcome in your Game
    Chosse one of our games
                1 : multiplication
                2 : rmove duplicate
                3 : exit''')
            user = int(input('Enter Game Number'))
            if user == 1:
                s1 = int(input('Enter Game Number'))
                e1 = int(input('Enter Game Number'))
                s2 = int(input('Enter Game Number'))
                e2 = int(input('Enter Game Number'))
                self.multi_application(s1,e1,s2,e2)
            elif user ==2:
                self.rmove_duplicate()
            elif user == 3:
            print('good bay')
                break
    def multi_application(self,start,end,s1,e1):
        for i in range(start,end+1):

            for j in range(s1,e1+1):
                 print(f'{i} * {j} = {i * j}')
            print('-'*50)


    def rmove_duplicate(self):
        userr = input('enter the name\n')
        u=[]
        for name in userr:
            if name not in u :
                u.append(name)
        print(*u)

g1 = Game()
"""



