from datetime import date
def main():

    today = date.today()
    d3 = today.strftime("%m/%d/%y")
    print(d3)
if __name__ == '__main__':
    main()