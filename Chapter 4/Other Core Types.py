## Other Core types

X = set('spam')             # Make a set out of a sequence in 2.X and 3.X
Y = {'h', 'a', 'm'}         # Make a set with set literals in 3.X and 2.7

X, Y                        # A tuple of two set without parentheses
X & Y                       # Intersection
X | Y                       # Union
X - Y                       # Difference
X > Y                       # Superset
print({n ** 2 for n in [1, 2, 3, 4]}) # Set comprehensions in 3.X and 2.7

print(list(set([1, 2, 1, 3, 1])))       # Filtering out duplicates (possibly reordered)
print(set('spam') - set('ham'))         # Finding differences in collection
print(set('spam') == set('asmp'))       # Order-neutral equality tests (== is False)
print('p' in set('spam'), 'p' in 'spam', 'ham' in ['eggs', 'spam', 'ham'])


print(1/3)

print((2/3) + (1/2))

import decimal

d = decimal.Decimal('3.141')
print(type(d + 1))
print(d + 1)

decimal.getcontext().prec = 2
print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))

from fractions import Fraction          # Fractions: numerator + denominator
f = Fraction(2, 3)

print(f + 1)

print(f + Fraction(1, 2))

## Booleans

print(1 > 2, 1 < 2)                     # Booleans


print(bool('spam'))                     # Object's Boolean value

print(bool())                           # No value == False

X = None                                # None placehold
print(X)

L = [None] * 100                        # Initialize a list of 100 Nones
print(L)

## How to break flexibility (not recommended)

print(type(L))                              # Class List
print(type(type(L)))                        # Class type

if type(L) == type([]):
    print('yes')

if type(L) == list:
    print('yes')

if isinstance(L, list):
    print('yes')

