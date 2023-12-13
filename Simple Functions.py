##### Nicholas Catani #####
###########################



#####################################################################
## Write a program to print the following series: 1, 4, 9, 16, 25, 36

# Number of terms defined in the series
series = 10
# Starting variable
current_term = 1
# Loop to generate and print the series
for _ in range(series):
    print(current_term ** 2, end=", ")
    current_term += 1 # Increase the next term by 2 to get the next square!



######################################################################
## Write a program to print the Fibonacci series until a defined limit

def fibonacci_series(limit):
    fib_series = []
    a, b = 0, 1
    while a <= limit:
        fib_series.append(a)
        a, b = b, a + b
    return fib_series
# Define the limit
limit = 500
# Call the function to generate and print the Fibonacci series
result = fibonacci_series(limit)
print("Fibonacci series up to", limit, ":")
print(result)



################################################################
## Write a program to count the number of vowels in a given word

def count_vowels(word):
    vowels = "AEIOUaeiou" # Define a string containing all vowels
    vowel_count = 0

    # Iterate through each character in the word
    for char in word:
        if char in vowels:
            vowel_count += 1
    return vowel_count
# Input word
word = input("Enter a word: ")
# Call the function to count vowels
num_vowels = count_vowels(word)
# Print the result
print("Number of vowels in the word:", num_vowels)



###############################################################################
## Write a program to calculate the sum of digits of a number entered by a user

def sum_of_digits(number):
    total = 0
    while number > 0:
        digit = number % 10  # Get the last digit
        total += digit       # Add the digit to the total
        number //= 10        # Remove the last digit
    return total
# Input a number from the user
try:
    num = int(input("Enter a number: "))
    if num < 0:
        raise ValueError("Please enter a non-negative integer.")
except ValueError as e:
    print(e)
else:
    digit_sum = sum_of_digits(num)
# Print the result
print("Sum of digits", digit_sum)



####################
## Print time & date

import datetime
now = datetime.datetime.now()
print("Current Date & Time", now)



##################################################################################
## Write a function to calculate the compound interest of a given principal amount

def calculate_compound_interest(principal, rate, time):
    # Calculate compound interest using the formula: A = P(1 + r/n)^(nt) - P
    # Where:
    # A = Final amount (Principal + Interest)
    # P = Principal amount
    # r = Annual interest rate (in decimal form, e.g., 0.05 for 5%)
    # n = Number of times interest is compounded per year
    # t = Time period (in years)
    n = 1
    amount = principal * (1 + rate / n) ** (n * time)
    compound_interest = amount - principal
    return compound_interest
# Input principal amount, interest rate, and time period from the user
try:
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the annual interest rate (as a decimal): "))
    time = float(input("Enter the time period (in years): "))
except ValueError:
    print("Please enter valid numeric values.")
else:
    interest = calculate_compound_interest(principal, rate, time)
    print("Compound interest", round(interest, 2))



####################################################################
## Write a program to count the number of spaces in a given sentence

def count_spaces(sentence):
    space_count = 0
    for char in sentence:
        if char == " ":
            space_count += 1
    return space_count
sentence = input("Enter a sentence: ")
space_count = count_spaces(sentence)
print("Number of spaces in the sentence:", space_count)



#################################################################
## Write a program to show only the even digits of a given number

def display_even_digits(number):
    even_digits = ""
    while number > 0:
        digit = number % 10     # Get the last digit
        if digit % 2 == 0:      # Check if the digit is even
            even_digits = str(digit) + even_digits
        number //= 10           # Remove the last digit
    return even_digits
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Please enter a valid numeric value.")
else:
    even_digits_result = display_even_digits(num)

    if even_digits_result:
        print("Even digits in the number:", even_digits_result)
    else:
        print("There are no even digits in the number.")



#################################################################
## Write a program to check whether a number is palindrome or not

def is_palindrome(number):
    original_number = number
    reversed_number = 0

    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number //= 10
    return original_number == reversed_number
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Please enter a valid numeric value.")
else:
    if is_palindrome(num):
        print(f"{num} is a palindrome.")
    else:
        print(f"{num} is not a palindrome.")



#################################################
## Write a program to print the following pattern

def print_pattern(n):
    for i in range(1, n + 1):
        for j in range(n - i):
            print(" ", end="\t")
        for j in range(2 * i - 1):
            if j % 2 == 0:
                print("*", end="\t")
            else:
                print("*", end="\t")
        print()
n = 3
print_pattern(n)



################################################################################
## Convert decimal number to hexadecimal number using print() output formatting.

decimal_number = 10
hexadecimal = hex(decimal_number)
print(f"Hexademical : {hexadecimal[2:]}")



###################################################################
## Write a program to accept any three string from one input() only

input_string = input("Enter three strings, separated by spaces: ")
str1, str2, str3 = input_string.split()
print("String 1", str1)
print("String 2", str2)
print("String 3", str3)



###################################################################
## Write a program to print a sentence using string.Format() method

format_string = "Hello, my name is {}. I am {} years old and I live in {}."
name = "Nicholas"
age = 30
city = "Seattle"
sentence = format_string.format(name, age, city)
print(sentence)



#########################################################################
## Write a program to read a file and print the second line from the file

file_name = "your_file.txt"
with open(file_name, "r") as file:
    lines = file.readlines()
    if len(lines) >= 2:
        print(lines[1].strip())
    else:
        print("The file does not have a second line.")



######################################################################
## Write a program to display the prime numbers of a range of numbers.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def print_primes(start, end):
    for number in range(start, end + 1):
        if is_prime(number):
            print(number, end=" ")
start = 1
end = 100
print_primes(start, end)



################################################################
## Write a program to print alternate alphabet of a given string

def print_alternate_characters(s):
    alternate_chars = s[::2]
    print(alternate_chars)
input_string = "What a wonderful day!"
print_alternate_characters(input_string)



#####################################################################
## Write a program to count alphabets, digits, and special characters

def count_characters(s):
    alphabets = digits = special = 0
    for char in s:
        if char.isalpha():
            alphabets += 1
        elif char.isdigit():
            digits += 1
        else:
            special += 1
    print(f"Alphabets: {alphabets}, Digits: {digits}, Special Characters: {special}")
sentence = ""
count_characters(sentence)



###############################################################
## Write a program to print the occurrence of a given substring

def count_substring(s, substring):
    count = s.count(substring)
    print(f"The substring '{substring}' occurs {count} times.")
string = ""
substring = ""
count_substring(string, substring)



#################################################################
## Write a program to print the middle alphabet of a given string

def print_middle_character(s):
    middle = len(s) // 2
    if len(s) % 2 == 0:
        middle_chars = s[middle - 1:middle + 1]
        print(f"Middle characters: {middle_chars}")
    else:
        print(f"Middle characters: {s[middle]}")
string = ""
print_middle_character(string)