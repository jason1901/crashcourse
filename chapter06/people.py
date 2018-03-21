person_0 = {
    'first_name': 'gary',
    'last_name': 'oldman',
    'age': 59,
    'birth_place': 'london, england'
}

person_1 = {
    'first_name': 'tom',
    'last_name': 'hanks',
    'age': 61,
    'birth_place': 'california, united states'
}

person_2 = {
    'first_name': 'tom',
    'last_name': 'hardy',
    'age': 40,
    'birth_place': 'london, england'
}

people = [person_0, person_1, person_2]

for person in people:
    print(person['first_name'].title() + ' ' + person['last_name'].title() + ':')
    print('\tAge: ' + str(person['age']))
    print('\tBirthplace: ' + person['birth_place'].title())