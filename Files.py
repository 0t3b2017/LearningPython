## Files
"""
# Write a file
f = open('data.txt', 'w')  # Make a new file in output mode ('w' is write)
f.write('Hello\n')  # Write string of characters to it
f.write('world\n')
f.close()  # Close to flush output buffers to disk

# Read a file
f = open('data.txt')  # 'r' (read) is the default processing mode
text = f.read()  # Read entire file into a string
print(text)  # print interprets control characters

print(text.split())  # File content is always a string
print(text.upper())
print(type(text))

print('#' * 20, '\n')

for line in open('data.txt'):
    print(line)


## Getting help

print(type(f))

# print(dir(f))

# print(help(f.seek))

"""

## Binary Bytes Files

import struct
packed = struct.pack('>i4sh', 7, b'spam', 8)    # Create packed binary data
print(packed)                                   # 10 Bytes, not objects or text
print(len(packed))

file = open('data.bin', 'wb')                   # Open binary output file
file.write(packed)                              # Write packed binary data
file.close()

data = open('data.bin', 'rb').read()            # Open/read binary data file
print(data)                                     # Print 10 bytes, unaltered

print(data[4:8])                                # Slice bytes in the middle

print(list(data))                               # A sequence of 8-bit bytes

print(struct.unpack('>i4sh', data))             # Unpack into objects again

