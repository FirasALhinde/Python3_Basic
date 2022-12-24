'''
class Member:
    def __init__(self):
        print('new memer add')


m1 = Member()
Member()
Member()
Member()
print(m1.__class__)
'''

# class Member:
#     fake_name =['zer','pop','gassas']
#     user_count = 0
#     @classmethod
#     def show_user_count(cls):
#         return cls.user_count
#     def __init__(self,f_name,m_name,l_name,gender):
#         self.fname = f_name
#         self.mname = m_name
#         self.lname = l_name
#         self.gender = gender
#         Member.user_count +=1
#     def get_full_name(self):
#         if self.fname in Member.fake_name:
#             raise ValueError('name not allowad')
#         return (f'Hello {self.fname} {self.mname} {self.lname}')
#     @staticmethod
#     def say_hello():
#         print('hello firas')
#     def name_with_title(self):
#         if self.gender == 'Male':
#             return f'Hello Mr {self.fname}'
#         else:
#             return f'Hello MS {self.fname}'

#     def full_name(self):
#         return f'{self.name_with_title()} Is full name is {self.get_full_name()}'

#     def delete_user(self):
#         Member.user_count-=1
#         return f' delet user : {self.fname}'


# print(Member.user_count)   
# m1= Member('Jad','Khaldoun','Alhinde','Male')

# m2= Member('Firas','Khaldoun','Alhinde','Male')



# m3= Member('dd','Mohamed','Alsama','Famale')
# print(Member.user_count)
# print(m3.delete_user())
# print(Member.user_count)
# print(Member.show_user_count())
# Member.say_hello()
# print(m1.__class__.__name__)
#print(dir(Member))
#m1.get_full_name()


# class Skille:
#     def __init__(self) -> None:
#         self.skile = ['html','css','python']

#     def __str__(self) -> str:
#         return self.skile[0]

#     def __len__(self):
#         return len(self.skile)

# p = Skille()
# print(p)
# print(len(p))
# p.skile.append('php')
# p.skile.append('js');print(len(p))


# class Food:
#     def __init__(self,name,price) -> None:
#         self.name=name
#         self.price =price
#         print(f"{name} is created base class {price}")
    
#     def eat(self):
#         print('eat method from base class')
    

# class Apple(Food):
#     def __init__(self,name,price) -> None:
#         #Food.__init__(self,name)
#         super().__init__(name,price)
#         print(f"{self.name} is created dirived class {self.price}")


# #f1 = Food('pizza')
# a1 = Apple('pizza',3333)
# # a1.e


# class A:
#     def s(self):
#         print('A')
#         raise NotImplementedError('assad')
# class B(A):
#     def s(self):
#         print('B')
#     # pass
# class C:
#     pass

# b = B()
# b.s()


# class Member:
#     def __init__(self,name,age) -> None:
#         self.__name = name
#         self.__age =age
#     def get_name(self):
#         return self.__name
    
#     def set_name(self,new_name):
#         self.__name = new_name
#     @property
#     def say_hello(self):
#         return f'Hello {self.__name}'
    
#     def age_in_days(self):
#         return self.__age * 365

# one = Member('Firas',24)

# print(one.say_hello)

from abc import ABCMeta,abstractclassmethod
class Programing(metaclass =ABCMeta):
    @abstractclassmethod
    def has_oop(self):
        pass

class Python(Programing):
    pass

class Pascakl(Programing):
    def has_oop(self):
        return 'No'

one = Python()
print(one.has_oop())