import my_programs

def choice_chooser():
    while True:
        print("------ FUNCTION MENU ------")
        print("1. Swap Two Numbers")
        print("2. GCD of two numbers")
        print("3. Custom Sorting")
        print("4. Reverse a string")
        print("5. Sum of digit")
        print("6. Vowel count in a string")
        print("7. Words count")
        print("8. String convert to title case")
        print("9. Palindrome check")
        print("10. Prime Number check")
        print("11. Factorial")
        print("12. Decimal to Binary")
        print("13. Find the largest of three numbers")
        print("14. Remove duplicates from a list")
        print("15. Exit")

        choice = input("Choose the correct option: ")

        if choice == "1":
            a = int(input("Enter the First number: "))
            b = int(input("Enter the second number: "))
            a, b = my_programs.swap(a,b)
            print(f' After swapping: a = {a}, b= {b}')

        elif choice == "2":
            a = int(input("Enter the first number: "))
            b = int(input("Enter the second number: "))
            gcd = my_programs.gcd(a, b)
            print(f'GCD of {a} and {b} is {gcd}')

        elif choice == "3":
            words = input("Enter the words: ").split(",")
            sort = my_programs.sort(words)
            print("Sorted list: ", sort)

        elif choice == "4":
            a = input("Enter the word: ")
            reverse = my_programs.reverse(a)
            print("Reversed string", reverse)

        elif choice == "5":
            n = int(input("Enter the number: "))
            print("Sum", my_programs.sum(n))

        elif choice == "6":
            sentence = input("Enter the sentence: ")
            print("Number of vowels: ", my_programs.count(sentence))

        elif choice == "7":
            sentence = input("Enter the sentence: ")
            print("Number of words: ", my_programs.count_word(sentence))

        elif choice == "8":
            sentence = input("Enter the sentence: ")
            print("Title case: ", my_programs.convert(sentence))

        elif choice == "9":
            a = input("Enter the string: ")
            if my_programs.palindrome(a):
                print(f'{a} is a palindrone')
            else:
                print(f'{a} is not palindrome')

        elif choice == "10":
            n = int(input("Enter the number: "))
            if my_programs.prime(n):
                print(f'{n} is a Prime Number')
            else:
                print(f'{n} is not Prime')

        elif choice == "11":
            n = int(input("Enter the number: "))
            print("Factorial: ", my_programs.factorial(n))

        elif choice == "12":
            n = int(input("Enter the decimal number: "))
            print("Binary is", my_programs.decimal_to_binary(n))

        elif choice == "13":
            a = int(input("Enter the First number: "))
            b = int(input("Enter the second number: "))
            c = int(input("Enter the Third number: "))
            print("Largest Number is: ", my_programs.largest(a, b, c))

        elif choice == "14":
            list = input("Enter the string: ").split(",")
            print("List after removing Duplicates: ", my_programs.duplicates(list))

        elif choice == "15":
            print("Exiting...")
            break

        else:
            print("Enter only valid option")

        
choice_chooser()












            
