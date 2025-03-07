
#正序
cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)
#倒序
cars = ['bmw','audi','toyota','subaru']
cars.sort(reverse=True)
print(cars)
#不改变原序
cars = ['bmw','audi','toyota','subaru']
print('Here is original list:')
print(cars)
print('\nHere is sorted list:')
print(sorted(cars))
print('\nHere is original list again:')
print(cars)
#倒序不改变原序
cars = ['bmw','audi','toyota','subaru']
print('Here is original list:')
print(cars)
print('\nHere is sorted list:')
print(sorted(cars,reverse=True))
print('\nHere is original list again:')
print(cars)
#列表元素反转
cars = ['bmw','audi','toyota','subaru']
cars.reverse()
print(cars)
#列表长度
cars = ['bmw','audi','toyota','subaru']
len = len(cars)
print(len)