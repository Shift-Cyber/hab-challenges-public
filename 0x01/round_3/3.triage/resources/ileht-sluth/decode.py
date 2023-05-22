#!/usr/bin/python3

ITERATIONS = 5

morse_table = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': '/', '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.',
    '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-',
    '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', '': ''
}
morse_table_inverted = {v: k for k, v in morse_table.items()}

def ascii_to_morse(text:str): return '/'.join([ morse_table[char] for char in text ])
def morse_to_ascii(text:str): return ''.join([ morse_table_inverted[morse_word] for morse_word in text.split('/')])

with open('morse.txt', 'r') as fio:
    old_value, new_value = fio.read().strip(), None
    
    while True:
        try:
            new_value = ''.join([morse_to_ascii(word) for word in old_value.split('/')])
            old_value = new_value
        except: #we cant morse decode ascii chars, so we have the flag... exit
            print(new_value)
            exit()

