import random
import time
import re


def main_menu():
    time.sleep(1)
    print("MAIN MENU")
    print("1. String Operation")
    print("2. Number Operation")
    print("3. Factorial Sum Calculator")
    print("4. Palindrome Checker")
    print("5. Prime Number Checker")
    print("6. Email Checking")
    print("7. EXIT")


def main():
    while (True):
        main_menu()
        choice = input('\nEnter choice(1, 2, 3, 4, 5, 6, or 7): ')
        print()

        if choice == '1':
            while True:
                rchoice = input('Choice(1-> Email Validation, 2-> Random Number Generator, 3-> Pyramid, 4-> Convert to Uppercase, 5-> Convert to Lowercase, 6-> Back to Main Menu): ')
                print()
                if rchoice == '1':
                    email = input("\nEnter an email address: ")
                    # Enhanced email checking loop
                    while not fnEmailValidation(email):
                        print(f"\nError: Provided email address [{email}] is not valid. Please try again.")
                        email = input("Re-enter a valid email address: ")
                    print(f"\nProvided email address [{email}] is valid")  # If email is valid

                elif rchoice == '2':
                    filename = "outputFile.txt"  
                    write_lines_to_file(filename)

                elif rchoice == '3':
                    n = int(input("How many rows for the pyramid? "))
                    createPyramid(n)

                elif rchoice == '4':
                    text = input("Enter a string: ")
                    print(f"Uppercase string: {fnConvertToUppercase(text)}")

                elif rchoice == '5':
                    text = input("Enter a string: ")
                    print(f"Lowercase string: {fnConvertToLowercase(text)}")

                elif rchoice == '6':
                    break
                else:
                    print('\nInvalid input !!!')
                print()

        elif choice == '2':
            while True:
                print("\n1 for Number Reverse")
                print("\n2 for Fibonacci Series")
                print("\n3 for Find Factorial of a Number")
                print("\n4 for Even Number Set")
                print("\n5 for Odd Number Set")
                print("\n6 for Greatest number between 3")
                print("\n7 for Lower number between 3")
                print("\n8 for Generate 100 Random Numbers and write in a file")
                echoice = input('\nEnter choice(1-8): ')
                print()
                if echoice == '1':
                    fnReverseNumber()

                elif echoice == '2':
                    fibo()

                elif echoice == '3':
                    n = int(input("Enter a number: "))
                    print(f"Factorial of {n} is {fnFactorial(n)}")

                elif echoice == '4':
                    fnEvenNumberSet()

                elif echoice == '5':
                    fnOddNumberSet()

                elif echoice == '6':
                    x = int(input("Enter a number: "))
                    y = int(input("Enter a number: "))
                    z = int(input("Enter a number: "))
                    print(f"Greatest number between {x}, {y}, and {z} is {max_of_three(x, y, z)}")

                elif echoice == '7':
                    x = int(input("Enter a number: "))
                    y = int(input("Enter a number: "))
                    z = int(input("Enter a number: "))
                    print(f"Lower number between {x}, {y}, and {z} is {min_of_three(x, y, z)}")

                elif echoice == '8':
                    fnRandomNumberGenerator()
                else:
                    print('\nInvalid input !!!')
                    break

        elif choice == '3':
            number = int(input("Enter a number: "))
            print(f"The sum of factorials of digits of {number} is {fnFactorialSum(number)}")  

        elif choice == '4':  
            user_input = input("Enter a string or number to check if it's a palindrome: ")
            if fnPalindromeChecker(user_input):
                print(f"'{user_input}' is a palindrome.")
            else:
                print(f"'{user_input}' is not a palindrome.")

        elif choice == '5':  
            number = int(input("Enter a number to check if it's prime: "))
            if fnPrimeNumberChecker(number):
                print(f"{number} is a prime number.")
            else:
                print(f"{number} is not a prime number.")
          
        elif choice == '6':  
            email = input("Enter an email address: ")
            if fnEmailValidation(email):
                print(f"\nProvided email address [{email}] is valid")
            else:
                print(f"\nProvided email address [{email}] is not valid")

        elif choice == '7':
            print('Thanks for using the program!')
            break

        else:
            print('Invalid input!!!')
            print()

def fnConvertToUppercase(text):
    return text.upper()

def fnConvertToLowercase(text):
    return text.lower()

def fnFactorialSum(number):
    return sum(fnFactorial(int(digit)) for digit in str(number))


def fnPrimeNumberChecker(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def fnPalindromeChecker(value):
    value = str(value).replace(" ", "").lower()
    return value == value[::-1]


def write_lines_to_file(filename):
    lines = []
    print("Enter multiple lines of text (type 'DONE' on a new line to finish):")
    while True:
        line = input()
        if line.strip().upper() == "DONE":
            break
        lines.append(line)
    with open(filename, "w") as file:
        for line in lines:
            file.write(line + "\n")
        print(f"File [{filename}] has been saved successfully!")


def fnEvenNumberSet():
    print("Even numbers from 1 to N")
    n = int(input("Enter a number to set range: "))
    for i in range(2, n + 1, 2):
        print(i, end=" ")

def fnOddNumberSet():
    print("Odd numbers from 1 to N")
    n = int(input("Enter a number to set range: "))
    for i in range(1, n + 1, 2):
        print(i, end=" ")

def max_of_two(x, y):
    if x > y:
        return x
    return y

def min_of_three(x, y, z):
    return min(x, y, z)


def fnRandomNumberGenerator():
    with open("100Numbers.txt", "w") as file:
        for i in range(100):
            number = random.randint(1, 100)
            file.write(str(number) + " ")

    with open("100Numbers.txt", "r") as file:
        print(file.read())


def max_of_three(x, y, z):
    return max(x, y, z)


def fnEmailValidation(email):
    pattern = r"[^@]+@[^@]+\.[^@]+"
    return re.match(pattern, email) is not None


def createPyramid(n):
    for i in range(1, n+1):
        print("#" * i)
    for i in range(n-1, 0, -1):
        print("#" * i)


def fnFactorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fnFactorial(n - 1)


def fnReverseNumber():
    n = int(input("Enter a number: "))
    print(f"Reversed number: {str(n)[::-1]}")


def fibo():
    n = int(input("\nEnter a number for the series: "))
    a, b = 0, 1
    print(a, b, end=" ")
    for _ in range(n - 1):
        a, b = b, a + b
        print(b, end=" ")


main()