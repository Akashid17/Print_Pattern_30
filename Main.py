
def Display(iNo1,iNo2):

    if iNo1 == 0 or iNo2 == 0:
        if iNo1 == iNo2:
            print("Unable to Print Pattern, Both Values are Zero")
        elif iNo1 == 0:
            print("Unable to Print Pattern, Rows Count is Zero")
        elif iNo2 == 0:
            print("Unable to Print Pattern, Columns Count is Zero")    
    else:
        if iNo1 < 0:
            iNo1 = -iNo1
    
        if iNo2 < 0:
            iNo2 = -iNo2


        for x in range(iNo1):
            for y in range(iNo2):
                if x == 0 or y == 0 or x == iNo1-1 or y == iNo2-1 or x == y:
                    print("*",end="\t")
                else:
                    print("",end="\t")

            print()

def main():

    print("Enter Count of Rows and Columns")
    iValue1 = int(input())
    iValue2 = int(input())

    Display(iValue1,iValue2)

if __name__ == "__main__":
    main()