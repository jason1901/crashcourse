usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print('Logged in as admin, would you like to see a status report?')
        else:    
            print('Good after, ' + username)
else:
    print('We need to find more users!')