guests = ['spongebob squarepants', 'gary oldman', 'jeff goldblum']
print(guests[0].title() + ' can\'t make it because he doesn\'t exist.')
guests[0] = 'lebron james'
for item in guests:
    message = 'I invite you, ' + item.title() + ', to my dinner party on the 9th'
    print(message)