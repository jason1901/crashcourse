big_rivers = {
    'amazon': 'south america',
    'nile': 'africa',
    'yangtze': 'asia',
}

for river, location in big_rivers.items():
    print('The ' + river.title() + ' river is located in ' + location.title())

for river in big_rivers.keys():
    print(river.title())

for location in big_rivers.values():
    print(location.title())