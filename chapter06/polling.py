favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

people = ['josh', 'colby', 'jen', 'edward', 'katsuo']

for person in people:
    if person in favorite_languages.keys():
        print('Thanks for taking the poll, ' + person.title())
    else:
        print('Please take the poll ' + person.title())