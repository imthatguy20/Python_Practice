#!/usr/bin/python
"""
Lab 3: Three-Phase symmetric cipher
Goal: Create a program that implements Playfair cipher
Creator: Jerry Haynes

"""
print("Phase 1:\n")


plaintext = raw_input('Enter a message to encrypt: ')
print("You entered: " + plaintext)
ascii = []
for word in plaintext:
    ascii_word = []
    for char in word:
        ascii_word.append(ord(char))
    ascii.append(ascii_word)
print ascii

phase1key = raw_input('Enter first layer key: ')
print("You entered: " + phase1key)
New_phase1key = float(phase1key)

for x in ascii:
    print phase1key + x

"""""

for add in ascii:
    add += 39

#http://knowledgestockpile.blogspot.com/2011/01/string-formatting-in-python_09.html
char = []
for item in world_dict:
     if item[1] == 'House':
       price = float(item[2])
       prices.append(price)

print(price)

char = [('Fortran', 1954, 0.435,1000), ('Cobol', 1959, 0.391,1000),
              ('C', 1972, 16.076,1000), ('C++', 1980, 9.014,1000),
              ('Python', 1991, 6.482,1000),
              ('Java', 1995, 17.99,1000), ('C#', 2001, 6.687,1000)]


print "{0:<12} {1:^16} {2:^16} {3:>16}".format("Character",
                                        "ASCII",
                                        "X",
                                       "ASCII + X")
print "-"*63
for element in char:
    print "{0:12} {1:^16} {2:^16.2f} {3:>16}".format(element[0],
                                            element[1],
                                            element[2],
                                            element[3])
"""""