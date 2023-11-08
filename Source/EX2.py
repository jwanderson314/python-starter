#Create a program that uses the input() function to obtain the width, height and length of a box. 
#The program computes the volume of the box (width * height * length) and writes it to the console:

def main():
    width = input("Enter Width")
    height = input("Enter Height")
    length = input("Enter length")

    vol = float(width) * float(height) * float(length)

    print(f"Vol: {vol}")

if __name__ == '__main__':
    main()
    