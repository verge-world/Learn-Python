list = ['ham pizza','bacon pizza','sausage pizza']
friend_pizzas = list[:]
list.append('butter pizza')
friend_pizzas.append('basil pizza')
print("My favourite pizzas are:")
for pizza in list:
    print(pizza)
print("My friend's favourite pizzas are")
for pizzea in friend_pizzas:
    print(pizzea)