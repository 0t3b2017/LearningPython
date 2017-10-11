### Tuples are similar to lists, but immutable.

T = (1, 2, 3, 4)

print(len(T))

# Concatenation
print(T + (5, 6))

# Indexing, slicing, and more
print(T[0])
print(T.index(4))
print(T.count(4))

# Tuples are immutable
# T[0] = 2 ## This generates an error.

# make a new tuple for a new value
T = (2,) + T[1:]
print(T)

# Tuples with mixed types and nesting

T = 'spam', 3.0, [11, 22, 33]
print(T[0])

for i in T:
    print(type(i))

print('=+' * 15)

print(T[2][1])

# T.append(4) ## There's no attribute append on tuples
