'''
class Calc:
    def __init__(self,name):
        print(f'welcome {name}')
    def ssum(self,x,y):
        return x+y

    def mmulti(self,x,y):
        return x*y


#c1 = Calc('firas')
#print(c1.ssum(2,4))


class SciCalc(Calc):
    def power(self,x,y):
        return x**y


s1 = SciCalc('sdf')

print(s1.ssum(2,5))

print(s1.power(2,10))
'''
'''
class A:
    def do(self):
        print('in A')


class B(A):
    pass

class C:
    def do(self):
        print('in c')

class D(B,C):
    pass


d = D()
print(D.C.do())
'''
