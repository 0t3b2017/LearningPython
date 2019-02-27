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
"""

## Unicode Text Files

S = 'sp\xc4m'                                   # Non-ASCII Unicode text
print(S)
print(S[2])                                     # Sequence of characters

file = open('unidata.txt', 'w', encoding='utf-8') # Write/encode UTF-8 text

print(file.write(S))                            # 4 characters written

file.close()

text = open('unidata.txt', encoding='utf-8').read() # Read/decode UTF-8 text

print(text)                                     # Print 4 chars (code points)

print(len(text))

raw = open('unidata.txt', 'rb').read()          # Read raw encoded bytes

print(raw)                                      # Print the raw data

print(len(raw))                                 # It's really 5 bytes in UTF-8 (4 code points)

print(text.encode('utf-8'))                     # Manual encode to bytes

print(raw.decode('utf-8'))                      # Manual decode to str

print(text.encode('latin-1'))                   # Bytes differ in others
print(text.encode('utf-16'))

print(len(text.encode('latin-1')), len(text.encode('utf-16')))

print(b'\xff\xfes\x00p\x00\xc4\x00m\x00'.decode('utf-16'))  # But same string decoded

""" 
## Python 2.X

import codecs

X = codecs.open('unidata.txt', encoding='utf-8').read()
print(X)

open('unidata.txt', 'rb').read()

open('unidata.txt').read()
"""
