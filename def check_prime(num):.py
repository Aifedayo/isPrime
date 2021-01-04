def check_prime(num):
    prime_checker = False

    if num == 0:
        prime_checker = False
    elif num == 1 and num <=2:
        prime_checker = True
    if num > 1:
        for i in range(2, num):
            if (num % i == 0):
                prime_checker = True
                break

    if prime_checker:
        print(f'{num} is not a prime number')
    else:
        print(f'{num} is  a prime number')

check_prime(int(input('Input a value here: ')))
            