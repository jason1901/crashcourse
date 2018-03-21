favorite_numbers = {
    'jack': [12, 15, 32],
    'daniel': [3, 63, 2432],
    'meryl': [21, 21],
    'tom': [42, 42, 42, 42],
    'robert': [90, 19, 132, 119],
}

for person, number in favorite_numbers.items():
    print(person.title() + '\'s favorite numbers are:')
    print(number)