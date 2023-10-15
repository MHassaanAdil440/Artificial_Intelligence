#Accept two lists from the user and display their join
list1 = []
list2 = []
n = int(input("Enter n: "))
print("Enter 1st list: ")
for i in range(n):
    val = int(input("Enter list element "+str(i))+": ")
    list1.append(val)
print("Enter 2nd list: ")
for i in range(n):
    val = int(input("Enter list element "+str(i))+": ")
    list2.append(val)
list1.extend(list2)
print(list1)