import random

def main():
    num = random.randint(1, 100)
    if(num < 10):
        print(str(num) + ": and you lose")
    elif(num > 10 and num < 50):     
        print(str(num) + ": Try again")
    else:
        print(str(num) + ": You win!")
    

    
if __name__ == '__main__':
    main()