# mysum =(lambda num : num*num) (2)

# print(mysum)

# names = ['ali','firas','jad','basil','samera']

# mucount = []
# for nam in names:
#     mucount.append(len(nam))

# print(mucount)

# for name in map(lambda nam : len(nam),names):
#     print(name)
# numbers = [12,23,4,223,12,45]

# fil = filter(lambda num : num>50,numbers)
# print(*fil)
# numbers = [12,12,12,1,212,12]
# from functools import reduce


# red = reduce(lambda num1 ,num2 : num1+num2,numbers)
# print(red)


# names = ['firas','Khaldoun','Alhinde']
# print(' | '.join(names))


# path = 'my   &&&&  name &&&     firas &&&   alhinde'

# print(path.replace('&','').split())

# class Student:
#     def add_mark(self,mark):
# try:
#     age = int(input("enter your age: "))
#     print(100/age)
# except ValueError as e:
#     print("Enter the int please")
#     print(e)
# # except (ValueError,ZeroDivisionError)
# except ZeroDivisionError:
#     print('no Division Zero')
# else:
#     print("no exept")
# finally:
#     print("END")