# Write a Python function that checks whether a passed string is palindrome
def isPallindrome(phrase):
    phrase = phrase.replace(' ','')
    return phrase == phrase[::-1]

# Write a Python function that takes a number as a parameter and checks if the number is prime or not
def isPrime(number):
    for devisor in range(2,number//2):
        if number % devisor == 0:
            return False
    return True

# Write a Python function to check whether a number is in a given range
def isInRange(number,range_start,range_end):
    if number >= range_start and number <= range_end:
        return True
    else:
        return False

# Write a Python function to calculate the factorial of a number
def factorial(number):
    result = 1
    for i in range(1,number+1):
        result *= i
    return result

# Write a Python program to reverse a string
def reverse(string):
    return string[::-1]

# Write a Python function to sum all the numbers in a list
def sum(list):
    result = 0
    for number in list:
        if type(number) == int:
            result += number
        else:
            return False
    return result

# Write a Python function to find the Max of three numbers
def maximum(number1,number2,number3):
    return max(number1,number2,number3)

