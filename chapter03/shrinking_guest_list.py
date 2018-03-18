guests = [
    'kyrie irving', 'lebron james', 'sufjan stevens', 
    'gary oldman', 'jeff goldblum', 'jamie lannister'
    ]
print('I can only invite two people for dinner because I don\'t have enough food')

for item in range(4):
    uninvite = guests.pop()
    print('Sorry ' + uninvite.title() + ', you are uninvited to my dinner party.')

for item in guests:
    print(item.title() + ', you are still invited to my party.')

del guests[0]
del guests[0]
print(guests)