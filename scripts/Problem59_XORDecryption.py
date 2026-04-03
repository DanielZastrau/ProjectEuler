"""
https://projecteuler.net/problem=59
"""

from time import sleep

def main():
    with open('p059_cipher.txt', 'r') as file:
        for line in file:
            line_clean = [ int(elem) for elem in line.strip().split(',') ]

    for n1 in range(97, 123):
        for n2 in range(97, 123):
            for n3 in range(97, 123):
                values = [n1, n2, n3]
                key_text = []
                letter = 0

                for i in range(len(line_clean)):
                    key_text.append(values[letter])
                    letter = (letter + 1)%3

                Text = [ chr(line_clean[i] ^ key_text[i]) for i in range(len(line_clean)) ]
                Text = ''.join( Text )
                
                if Text.startswith('An extract taken from'):
                    Text = [ ord(elem) for elem in Text ]
                    return sum(Text)
                    
print(main())