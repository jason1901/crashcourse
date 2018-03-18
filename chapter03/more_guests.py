guests = ['lebron james', 'gary oldman', 'jeff goldblum']
print('i have found a bigger dinner table, so now i can invite more people')
guests.insert(0, 'kyrie irving')
guests.insert(2, 'sufjan stevens')
guests.append('jamie lannister')
for item in guests:
    message = 'I invite you, ' + item.title() + ', to my dinner party on the 9th'
    print(message)