items = [0, None, 0.0, True, 0, 7]
found = False # flag
for item in items:
    print('Scanning item', item)
    if item:
        found = True # update the flag
        break
if found:
    print('At least one item evaluates to True')
else:
    print('All items evaluates to False')



# Pythonic way
items = [0, None, 0.0, True, 0, 7]

if any(items):
    print('At least one item evaluates to True')
else:
    print('All items evaluates to False')
