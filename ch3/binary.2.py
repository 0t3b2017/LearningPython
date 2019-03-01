n = 255 # bin(255)
remainders = []
while n > 0:
    n, remainder = divmod(n, 2)
    remainders.append(remainder)

# reverse list
remainders = remainders[::-1]
print(remainders)
