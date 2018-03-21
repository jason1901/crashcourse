pets = [
    {
        'name': 'chop',
        'breed': 'pitbull',
        'owner': 'jason'
    },
    {
        'name': 'drogo',
        'breed': 'golden retriever',
        'owner': 'hai'
    },
    {
        'name': 'emma',
        'breed': 'golden retriever',
        'owner': 'rose'
    }
]

for pet in pets:
    print(pet['name'].title() + ' is a ' + pet['breed'] +
    ' and their owner is ' + pet['owner'].title())