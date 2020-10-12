def getPythagoreanTriplets(n):
    ''' This function takes an integer n, and returns a list of all possible Pythagorean Triplets within the range of ---> 1 to n'''
    result = []
    m =2
    c = 0
    while c < n:
        for i in range(1, m):
            a = m*m - i*i
            b = 2*m*i
            c = m*m + i*i
            if c > n:
                break
            result.append((a,b,c))
        m += 1
    return result


if __name__ == "__main__":
    n = int(input("Enter an integer number to get all possible Pythagorean Triplets : "))

    answer = getPythagoreanTriplets(n)
    if answer:
        print('\nAll Possibel Pythagorean Triplets within the range of 1 to {} are :'.format(n))
        for i in answer:
            print(i)
        print('')
    else:
        print('\nThere is no Pythagorean Triplets !!!\n')
