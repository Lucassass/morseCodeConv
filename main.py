from fromMorse import decrypt
from toMorse import encrypt

def main(): 
    file = open("file.txt") 
    result = encrypt(file.read()) 
    print (result) 
  
    file2 = open("file2.txt")
    result = decrypt(file2.read()) 
    print (result) 

# Executes the main function 
if __name__ == '__main__': 
    main()