def main():
    
    vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}


    vowelc = 0
    consonants = 0
    word = input("Enter string: ")
    for x in word:
        if(x in vowels):
            vowels += 1
        
        
    print("Vowels: " +  str(vowels))
    print("Consonants: " +  str(consonants))
    


if __name__ == '__main__':
    main()