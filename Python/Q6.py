def isPrime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0: 
                return False
        return True
    return False

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
for i in range(first_number, second_number+1):
    if isPrime(i):
        print(i)