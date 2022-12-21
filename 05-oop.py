class Calculator:
    def __init__(self,x,y,name):
        self.x = x
        self.y = y
        print(f'Hello {name}')
        print('in __init__ :: ',self.sum())
    def sum(self):
        return self.x+self.y
    def multi(self):
        return self.x*self.y

s = Calculator(12,12,'firas')
print(s.sum())
print(s.multi())
    
