import string

def encrypt():
    # holds all possible letters of the alphabet
    alphabet = string.ascii_letters
    # user can determine the number of times to shift
    shift = int(input("please input number of times to shift (should be a positive whole number): "))
    # input word to be encrypted
    prompt = str(input("please input word(s) to be encrypted: "))
    # get length of word to be encrypted
    length = len(prompt)
    # calculate the length of alphabet after removing number to be shifted by
    new = len(alphabet) - shift
    # letters after shifting the required number of times
    part1 = alphabet[new:]
    # letters moved by shifting process
    part2 = alphabet[0:new]
    # joining both parts
    new_alphabet = part1 + part2
    # empty array to hold alphabet after completing shift
    shifted_alphabet = []
    # empty array to hold encrypted string
    encrypted = []

    # function to perform encryption processing
    try:
        for y in range(len(alphabet)):
            shifted_alphabet.append(new_alphabet[y])
        
        for x in range(length):
            if prompt[x]==" ":
                encrypted.append(" ")
            else:
                position = alphabet.index(prompt[x])
                encrypted.append(shifted_alphabet[position])
    
        encrypted = "".join(encrypted)
        print(encrypted)
    except:
        print("invalid input, please type in a word")

encrypt()