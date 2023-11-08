
def main():
    myList = [6,2,7,3,77,7,1]
    small = myList[0]

    for x in myList:
        if(x < small):
            small = x

    print(small)

    

    
if __name__ == '__main__':
    main()