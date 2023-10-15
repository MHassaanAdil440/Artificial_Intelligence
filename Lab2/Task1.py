#Write loop where user input is added to sum
no_of_inputs = int(input("Enter the number of inputs: "))
i = 0
ans = 0
while i < no_of_inputs:
    number = int(input("Enter Number: "))
    ans += number
    i += 1
print(ans)