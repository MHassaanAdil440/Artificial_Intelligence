#input a list from the user and sort it using sort function
list = []
n = int(input("Enter the number of elements in the list: "))
for i in range(0,n):
    element = int(input("Enter element: "))
    list.append(element)

print("The list is: ", list)
list.sort()
print("The sorted list is: ", list)


