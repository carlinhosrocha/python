print("/////////////////////////")
print("//RESISTOR'S CALCULATOR//")
print("/////////////////////////")
print("")
#Variables
#-------------
black = 0
brown = 1
red   = 2
orange= 3
yellow= 4
green = 5
blue  = 6
purple= 7
gray  = 8
white = 9
gold =  10
silver = 11
cont = 'S'
#-------------
#Strings variables
o = 'Ohms.'
kilo = 'KOhms.'
mega = 'MOhms.'
#----------------
#Resistors Colors
print("=======================================")
print("= ENTER with four resistor's colors:  =")
print("=======================================")
while (cont == 'S') or (cont == 's'):

     print("=================")
     print("= BLACK...... 0 =")
     print("= BROWN...... 1 =")
     print("= RED........ 2 =")
     print("= ORANGE..... 3 =")
     print("= YELLOW..... 4 =")
     print("= GREEN...... 5 =")
     print("= BLUE....... 6 =")
     print("= PURPLE..... 7 =")
     print("= GRAY....... 8 =")
     print("= WHITE......9 =")
     print("= GOLD.......10 =")
     print("= SILVER.....11 =")
     print("=================")
     print("******************")
     color1 = int(input("Enter with color one: "))
     color2 = int(input("Enter with color two: "))
     color3 = int(input("Enter with color three: "))
     color4 = int(input("Enter with color four: "))
     resistor = ((color1*10) + color2) * (10**color3)
     #Engineering Notation
     #resistor = (resistor/1000) if (resistor >= 1000) else resistor
     if (resistor < 1000):
          print("***********************************************")
          print("The value of the resistor is ",resistor, "Ohms.")
          print("***********************************************")
          #variation
          var_Gold = (0.05*resistor)
          var_Silver = (0.1*resistor)
          tax1 = (resistor + var_Gold) if (color4 == 10) else (resistor + var_Silver)
          tax2 = (resistor - var_Gold) if (color4 == 10) else (resistor - var_Silver)
          print("The tax of variation for a resistor of ", resistor, "Ohms is: ")
          print("===============================================================")
          print("-",tax2,"Ohms----------",resistor,"Ohms-----------",tax1,"Ohms-")
          print("===============================================================")
     elif (resistor >= 1000) and (resistor < 1000000):
          resistor = resistor/(10**3)
          print("*************************************************")
          print("The value of the resistor is ", resistor, "kOhms.")
          print("*************************************************")
          #variation
          var_Gold = (0.05*resistor)
          var_Silver = (0.1*resistor)
          tax1 = (resistor + var_Gold) if (color4 == 10) else (resistor + var_Silver)
          tax2 = (resistor - var_Gold) if (color4 == 10) else (resistor - var_Silver)
          print("The tax of variation for a resistor of ", resistor, "kOhms is: ")
          print("==================================================================")
          print("-",tax2,"kOhms----------",resistor,"kOhms-----------",tax1,"kOhms-")
          print("==================================================================")
     elif (resistor > 1000000):
          resistor = resistor/(10**6)
          print("*************************************************")
          print("The value of the resistor is ", resistor, "MOhms.")
          print("*************************************************")
          #variation
          var_Gold = (0.05*resistor)
          var_Silver = (0.1*resistor)
          tax1 = (resistor + var_Gold) if (color4 == 10) else (resistor + var_Silver)
          tax2 = (resistor - var_Gold) if (color4 == 10) else (resistor - var_Silver)
          print("The tax of variation for a resistor of ", resistor, "MOhms is: ")
          print("==================================================================")
          print("-",tax2,"MOhms----------",resistor,"MOhms-----------",tax1,"MOhms-")
          print("==================================================================")
     cont = str(input("Do you want to continue for anothers resisitors? [S/N]"))
else:
     out = input("Click ENTER to leave program...")
     

     
