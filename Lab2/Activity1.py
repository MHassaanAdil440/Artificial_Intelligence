marks = int(input("Enter Student marks: "))
if marks>=1 and marks<=100:
    if marks<50:
        print("Failed! Grade F.")
    elif marks>=51 and marks<=60:
        print("Grade E.")
    elif marks>=61 and marks<=70:
        print("Grade D.")
    elif marks>=71 and marks<=80:
        print("Grade C.")
    elif marks>=81 and marks<90:
        print("Grade B.")
    else:
        print("Grade A, ConGo")
else:
    print("Enter marks between 1 to 100.")