#Take two list form the user and join them using + operator
list1 = []
list2 = []
n = int(input("Enter the number of elements in the list1: "))
for i in range(0,n):
    element = int(input("Enter element: "))
    list1.append(element)
print("The list1 is: ", list1)

n = int(input("Enter the number of elements in the list2: "))
for i in range(0,n):
    element = int(input("Enter element: "))
    list2.append(element)
print("The list2 is: ", list2)

list3 = list1 + list2
print("The joined list is: ", list3)

