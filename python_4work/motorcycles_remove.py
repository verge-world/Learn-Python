motorcycles = ['honda','yamaha','suzuki','ducart']
print(motorcycles)
too_expensive = 'ducart'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")
# remove只会删除一个指定值，如需全部删除需调用循环