n = 255
remainders = []
while n > 0:
    remainder = n % 2 # remainder
    remainders.append(remainder) # keep track of remainders
    n //= 2 # divide n by 2

# reverse remainders
remainders = remainders[::-1]
print(remainders)
print(len(remainders))
