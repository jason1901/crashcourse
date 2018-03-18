pizzas = ['hawaiian', 'buffalo chicken', 'supreme']
friend_pizzas = pizzas[:]

pizzas.append('veggie')
friend_pizzas.append('sourkraut')

print('my favorite pizzas are:')
for pizza in pizzas:
    print(pizza)

print('my friend\'s favorite pizzas are:')
for pizza in friend_pizzas:
    print(pizza)