def palindrome(string):
    if string == string[::-1]:
        print("The string is palindrome")
    else:
        print("The string is not palindrome")

string = input("Enter a string: ")
palindrome(string)

