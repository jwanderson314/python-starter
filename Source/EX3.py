#Create a program that accepts a list of numbers using the input() function and 
# writes True if the first and last numbers are the same, otherwise write False to the console.

def main():
    num = input("Enter numbers: ")
    myList = num.split(",")
    
    print(myList[0] == myList[len(myList)-1])

if __name__ == '__main__':
    main()
    