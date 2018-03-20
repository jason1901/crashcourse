current_users = ['widp', 'beaky', 'fraj', 'eggdrop', 'mazeto']
new_users = ['arnold', 'nedbat', 'Widp', 'garyoldman', 'fraj']

for user in new_users:
    if user in current_users:
        print(user + ' already taken, please use a different name')