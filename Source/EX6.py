
def main():
    mylist = [11, 100, 101, 999, 1001]
    reversedList = []
    
    
    count = len(mylist)
    while(count > 0):
        reversedList.append(mylist[count-1])
        count -= 1
    print(reversedList)
    
    
if __name__ == '__main__':
    main()