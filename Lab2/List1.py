#Write a program that inputs the numbers in the list and than sum the list

list = []
n = int(input("Enter the number of elements in the list: "))
for i in range(0,n):
    element = int(input("Enter element: "))
    list.append(element)
print("The list is: ", list)

sum = 0
for i in range(0,n):
    sum = sum + list[i]
print("The sum of the list is: ", sum)


