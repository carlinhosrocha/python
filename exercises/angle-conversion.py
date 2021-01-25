#Angle_Conversion#

print("==========================")
print("=     ANGLE CONVERSION   =")
print("==========================")
print("")
#table
print("*******************")
print("* [1] for degrees *")
print("* [2] for radians *")
print("* [3] for grads   *")
print("*******************")
#pi_value
pi = 3.1415926536

num = int(input("Choose which unit will be converted: "))
if (num == 1):
     deg = int(input("Now, enter the value in degrees: "))
     #for radians
     rad = (pi*deg)/180
     #for grads
     gon = (10*deg)/9
     print("************************")
     print("* %.2f° = %.2f rad." %(deg, rad))
     print("* %.2f° = %.2f gon." %(deg, gon))
     print("************************")
     out = input("Click any botton for get out...")
if (num == 2):
     rad = float(input("Please, enter the value in radians: "))
     #for degrees
     deg = (180*rad)/pi
     #for grads
     gon = (200*rad)/pi
     print("************************")
     print("* %.2f° = %.2f°." %(rad, deg))
     print("* %.2f° = %.2f gon." %(rad, gon))
     print("************************")
     out = input("Click any botton for get out...")
if (num == 3):
     gon = float(input("Enter the velue in grads: "))
     #for degrees
     deg = 0.9*gon
     #for radians
     rad = (pi*gon)/200
     print("************************")
     print("* %.2f° = %.2f°." %(gon, deg))
     print("* %.2f° = %.2f rad." %(gon, rad))
     print("************************")
     out = input("Click any botton for get out...")
if (num != 1) or (num != 2) or (num != 3):
     print("THIS OPTION DON'T EXISTING!!!")
     print("RESTART THE PROGRAM AGAIN...")
     
