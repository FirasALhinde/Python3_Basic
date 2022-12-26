# import pyautogui as pyg
# pyg.moveTo(100, 150)
# pyg.alert('This is an alert box.')
# pyg.confirm('Enter option.', buttons=['A', 'B', 'C'])


# import datetime as dt

# from scheduler import Scheduler
# from scheduler.trigger import Monday, Tuesday
# import time

# def foo():
#     print("foo")

# schedule = Scheduler()

# # schedule.cyclic(dt.timedelta(minutes=10), foo)

# schedule.minutely(dt.time(second=5), foo)
# schedule.hourly(dt.time(minute=30, second=15), foo)
# schedule.daily(dt.time(hour=16, minute=30), foo)
# schedule.weekly(Monday(), foo)
# schedule.weekly(Monday(dt.time(hour=16, minute=30)), foo)

# schedule.once(dt.timedelta(minutes=10), foo)
# schedule.once(Tuesday(), foo)
# schedule.once(dt.datetime(year=2022, month=2, day=15, minute=45), foo)


# while True:
#     schedule.exec_jobs()
#     time.sleep(1)

# numbers = [12,23,9,6,34]

# ss = map(lambda num  : num*num,numbers)

# for n in ss:
#     print(n)

# for x in range(5):
#     for y in range(5):
#         print(f'{x} * {y} = {x*y}')

# 
numbers = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# x = numbers[0]
# y = numbers[1:-1]
# z = numbers[-1]
# print(x)
# print(y)
# print(z)

# h,n,*m = numbers

# print(h)
# print(n)
# print(m)