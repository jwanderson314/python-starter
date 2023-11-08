def main():
    first = ""
    second = ""
    while(True):
        first = input("Enter first integer: ")
        if(first=="exit"):
            break
        second = input("Enter second integer: ")
        if(second=="exit"):
            break
        sum = (int(first) + int(second))
        print("Answer: ", sum)
if __name__ == '__main__':
    main()
    