favorite_places = {
    'emma': ['london', 'tokyo', 'paris'],
    'jason': ['california'],
    'brandon': ['miami', 'germany']
}

for people, places in favorite_places.items():
    print('What are some of your favorite places, ' + people.title() + '?')
    print(places)