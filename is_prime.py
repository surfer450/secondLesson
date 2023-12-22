def is_prime():
    # function get number and find if rishoni
    num = input("enter number: ")
    num = int(num)

    if (num < 1):
        return False

    for i in range(2, num):
        if (num%i==0):
            return False
    return True



def main():
    try:
        print (is_prime())
    except ValueError as ve:
        print("error in file")

    except EOFError as ef:
        print("cant enter eof")




if __name__ == '__main__':
    main()

