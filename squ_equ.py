def squ_equ():
    #function gets 3 numbers as polinumes and find their answers
    a = int(input("enter number a: "))
    b = int(input("enter number b: "))
    c = int(input("enter number c: "))

    try:
        answer1 = (b*-1 + (b**2 -4*a*c)**0.5)/(2*a)
    except ZeroDivisionError as zd1:
        print("answer 1 was divided by 0!")
        return


    try:
        answer2 = (b *-1 - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    except ZeroDivisionError as zd2:
        print("answer 2 was divided by 0!")
        return

    print("the answers are: x1=" + str(answer1) +", x2="+ str(answer2))


def main():
    try:
        squ_equ()
    except ValueError as ve:
        print("error in file")

    except EOFError as ef:
        print("cant enter eof")




if __name__ == '__main__':
    main()