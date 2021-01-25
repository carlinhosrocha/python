print("===============================")
print("==== Logical_Operators 1.0 ====")
print("===============================")
print("")
#Global Variables

#First Preposition
n1 = float(input("Enter with a number: "))
print("--------------------------")
print("= [E]  for Equal         =")
print("= [D]  for Diferent      =")
print("= [L]  for Larger        =")
print("= [S]  for Smaller       =")
print("= [GE] for Greater/equal =")
print("= [SE] for Smaller/Equal =")
print("--------------------------")
operator1 = str(input("Choose an operator: "))
n2 = float(input("Now, enter with other number: "))
#Connetive
print("----------------------------")
print("= [A]  for And             =")
print("= [O]  for Or              =")
print("= [IT] for IF..., Then     =")
print("= [II] for IF, and only IF =")
print("----------------------------")
connective = str(input("Very good! Choose a connective: "))
#Second Preposition
n3 = float(input("Let's to the second proposition. Enter with a number: "))
print("--------------------------")
print("= [E]  for Equal         =")
print("= [D]  for Diferent      =")
print("= [L]  for Larger        =")
print("= [S]  for Smaller       =")
print("= [GE] for Greater/equal =")
print("= [SE] for Smaller/Equal =")
print("--------------------------")
operator2 = str(input("Choose a operator to the preposition: "))
n4 = float(input("Finaly, enter with the last number : "))

#Check composite proposition - 1
check1 = True if (n1 == n2) else False
check2 = True if (n1 != n2) else False
check3 = True if (n1 >  n2) else False
check4 = True if (n1 <  n2) else False
check5 = True if (n1 >= n2) else False
check6 = True if (n1 <= n2) else False
#Check composite proposition - 2
check7 = True if (n3 == n4) else False
check8 = True if (n3 != n4) else False
check9 = True if (n3 >  n4) else False
check10= True if (n3 <  n4) else False
check11= True if (n3 >= n4) else False
check12= True if (n3 <= n4) else False     
#Conditions
if (connective == 'A'):
     if (operator1 == 'E'):
          if (operator2 == 'E'):
               if (check1 == True) and (check7 == True):
                    print("%.2f = %.2f AND %.2f = %.2f" %(n1, n2, n3, n4))
                    print(" The sentence is TRUE!!!")
                   
out = input("Click ENTER to exit: ")

