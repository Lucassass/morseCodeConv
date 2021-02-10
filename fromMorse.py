MorseDict = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'} 

# Function to decrypt a file from morse to english
def decrypt(file):
    file += ' '
    decipher = '' 
    citext = '' 
    for letter in file:
        # checks for space 
        if (letter != ' '): 
            # counter to keep track of space 
            i = 0
  
            # storing morse code of a single character 
            citext += letter 
  
        # in case of space 
        else: 
            # i = 1 indicates new character 
            i += 1
  
            # i = 2 indicates new word 
            if i == 2 : 
  
                 # adding space to separate words 
                decipher += ' '
            else: 
                # accessing the keys using their values (reverse of encryption) 
                decipher += list(MorseDict.keys())[list(MorseDict.values()).index(citext)] 
                citext = '' 
  
    return decipher 