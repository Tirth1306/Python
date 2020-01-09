# Write a function that takes two numbers as input parametersand returns True or False depending on whether they are co-primes.
# Two numbers are said to be co-prime if they do not
# have any common divisor other than one.
import math

def check_coprimes(a,b):
    if math.gcd(a,b)!=1 :
        print ("Numbers are not Co-prime!")

    else: print ("Numbers are Co-prime!")

a=int(input("Enter Number 1 :"))
b=int(input("Enter Number 2 :"))

check_coprimes(a,b)