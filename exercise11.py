
# This function takes the input from the User and returns the number if it is greater than 2
def get_number(question="Give me a number greater than 2: "):
    while True:
        try:
            n = int(input(question))
            if n >= 3:
                return n
        except ValueError:
            print("Please enter a valid integer") 


# This function takes a number as input and returns a list of divisors of the number
def get_divisors(n):
    x = list(range(2, n))
    divisors = [i for i in x if n % i == 0]
    return divisors


# main code with logic if list of divor is empty then the number is prime else not prime
n = get_number()
divisors = get_divisors(n)
if divisors == []:
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number, its divisors are {divisors}")