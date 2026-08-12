"""
project_functions.py
This module contains all the user-defined functions
for the Project B mini-project (function-based programs).
"""


def swap_two_numbers(a, b):
    """Swaps two numbers using a temporary variable"""
    temp = a
    a = b
    b = temp
    return a, b


def find_gcd(a, b):
    """Finds GCD of two numbers using a loop"""
    gcd = 1
    smaller = a if a < b else b
    for i in range(1, smaller + 1):
        if a % i == 0 and b % i == 0:
            gcd = i
    return gcd


def custom_sort(lst):
    """Sorts a list of strings by their length using selection sort"""
    sorted_list = list(lst)
    n = len(sorted_list)

    for i in range(n):
        smallest_index = i
        for j in range(i + 1, n):
            if len(sorted_list[j]) < len(sorted_list[smallest_index]):
                smallest_index = j
        temp = sorted_list[i]
        sorted_list[i] = sorted_list[smallest_index]
        sorted_list[smallest_index] = temp

    return sorted_list


def reverse_string(s):
    """Reverses a string using a loop"""
    reversed_str = ""
    for ch in s:
        reversed_str = ch + reversed_str
    return reversed_str


def sum_of_digits(n):
    """Finds sum of digits of a number using while loop"""
    n = abs(n)
    total = 0
    while n > 0:
        digit = n % 10
        total = total + digit
        n = n // 10
    return total


def count_vowels(sentence):
    """Counts number of vowels in a sentence"""
    vowels = "aeiouAEIOU"
    count = 0
    for ch in sentence:
        if ch in vowels:
            count = count + 1
    return count


def convert_title_case(sentence):
    """Converts a sentence to title case"""
    return sentence.title()


def check_palindrome(s):
    """Checks whether a string is a palindrome"""
    reversed_s = reverse_string(s)
    if s == reversed_s:
        return True
    else:
        return False


def check_prime(n):
    """Checks whether a number is prime using a loop"""
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def find_factorial(n):
    """Finds factorial of a number using recursion"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * find_factorial(n - 1)


def decimal_to_binary(n):
    """Converts a decimal number to binary using while loop"""
    if n == 0:
        return "0"

    binary = ""
    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n = n // 2
    return binary


def find_largest_of_three(a, b, c):
    """Finds the largest of three numbers using if-elif-else"""
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


def remove_duplicates(lst):
    """Removes duplicate elements from a list, keeping first occurrence"""
    single_list = []
    for item in lst:
        if item not in single_list:
            single_list.append(item)
    return single_list
