customers = [
        dict(id=1, total=200, cupon_code='F20'), # fixed 20
        dict(id=2, total=150, cupon_code='P30'), # percent 30
        dict(id=3, total=100, cupon_code='P50'), # percent 50
        dict(id=4, total=110, cupon_code='F15'), # fixed 15
        ]

for customer in customers:
    code = customer['cupon_code']
    if code == 'F20':
        customer['discount'] = 20.0
    elif code == 'F15':
        customer['discount'] = 15.0
    elif code == 'P30':
        customer['discount'] = customer['total'] * 0.3
    elif code == 'P50':
        customer['discount'] = customer['total'] * 0.5
    else:
        customer['discount'] = 0.0

for customer in customers:
    print(customer['id'], customer['total'], customer['discount'])


