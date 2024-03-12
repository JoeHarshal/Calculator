#Printing the title 
print("Basic Calculator")

#taking input from the user 
n1 = float(input("Enter the 1st number :- "))
n2 = float(input("Enter the 2nd number :- "))

# asking user's choice of operation
print("Press 1 for addition \n Press 2 for subtraction \n Press 3 for multiplication \n Press 4 for division")
  
choice = int(input("Enter your choice:- "))

# conditions
if choice == 1 :
    print(n1+n2)


elif choice == 2 :
    print("N1 - N2 =", n1-n2)
    print("N2 - N1 =", n2-n1)

elif choice == 3:
    print(n1*n2)


else :
    print("N1 / N2 =", n1/n2)
    print("N2 / N1 =", n2/n1)
