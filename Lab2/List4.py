#input a list and search the specifice element in the list

list = []
n = int(input("Enter the number of elements in the list: "))
for i in range(0,n):
    element = int(input("Enter element: "))
    list.append(element)
print("The list is: ", list)

search = int(input("Enter the element to be searched: "))
flag = 0
for i in range(0,n):
    if list[i] == search:
        flag = 1
        break
if flag == 1:
    print("Element found at index: ", i)
else:
    print("Element not found")


