cities = {
    'boston': {
        'country': 'united states',
        'population': '673,184',
        'fact': 'happy hours are against the law here',
    },
    'houston': {
        'country': 'united states',
        'population': '2.303 million',
        'fact': 'slightly smaller than massachusetts',
    },
    'cleveland': {
        'country': 'united states',
        'population': '385,809',
        'fact': 'originally named cleaveland',
    },
}

for city, stat in cities.items():
    print(city.title())
    for item, value in stat.items():
        print(item.title() + ': ' + value.title())