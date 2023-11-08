

def main():
    myList = [1,2,3]
    mySet = {3,4,5}
    for x in myList:
        mySet.add(myList[x-1])
    print(mySet)

if __name__ == '__main__':
    main()