def has_digit_d(num, d):
    num = str(num)

    for digit in num:
        if int(digit) == d:
            return True
    
    return False

if __name__ == '__main__':
    print("Enter value of n")
    n = int(input())

    print("Enter value of d")
    d = int(input())

    ans = 0

    print("The integers between 0 and n having digit d are:")
    for i in range(0, n+1):
        if(has_digit_d(i, d)==True):
            print(i)
            ans += 1

    print("Number of integer between 0 and", n, "having digit", d, "is:", ans)
