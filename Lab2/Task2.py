#Write program to find if number is prime

number = int(input("Enter number: "))
i = 2
while i < number:
    if number % i == 0:
        print("Not Prime")
        break
    i += 1
else:
    print("Prime")
    