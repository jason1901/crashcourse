cities = ['new york', 'los angeles', 'chicago', 'houston', 'philadelphia']
cities.append('phoenix')
cities.insert(0, 'dallas')
del cities[3]
cities.pop()
cities.remove('houston')
print(sorted(cities))
cities.sort()
cities.reverse()
print(cities)
print(len(cities))