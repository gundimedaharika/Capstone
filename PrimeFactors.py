def primeFactorize(n,factors):
    n = int(n)
    for x in range(2,n+1):
        if n%x == 0:
            factors.append(str(x))
            n = n//x
            if n == 1:
                return '*'.join(factors)
            else:
                return primeFactorize(n,factors)

if __name__ == '__main__':
    print("************PRIME FACTORS**************")
    print("Enter the numbers to calculate prime factors or enter 'quit' to exit")
    while True:
        print("Enter >>> ", end='')
        num = input()
        factors = []
        if num:
            if num.isdigit() == True:
                print(primeFactorize(num,factors))
            elif num == 'quit':
                break
            else:
                print('Please Enter Integer!!!!')
                continue
