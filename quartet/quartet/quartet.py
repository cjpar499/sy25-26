A1 = ["a1", "hundai accent wrc", 220,("221/300"), 5500,5.4,1998,4]
G2= ["g2", "Seat Ibiza", 220,("205/280"), 8400,6.5,1984,4]
F3 = ["F3", "Renault Megane", 218,("198/270"), 8400,5.9,1995,4]
A2= ["A2", "Ford Focus WRC", 224,("221/300"), 5400,5.5,1995,4]
F2=["F2", "Mitsubishi Galant", 180,("216/294"), 5800,6.3,3395,4]
D4=["D4", "Peugeot 206 WRC", 225,("221/300"), 5600,5.4,1996,4]
H2=["H2", "Mitsubishi Lancer", 198,("213/290"), 5500,7.2,1997,4]
G1=["G1", "Citroen Visa 4x4", 190,("74/100"), 7680,9,1556,4]
E4=["E4", "Austin Metr0 6", 240,("265/360"), 9800,3.4,3600,6]
G3=["G3", "Mitsubishi Pajero", 185,("153/208"), 7000,9.6,3497,6]
C4=["C4", "Citreon Saxo kit car", 168,("161/220"), 7000,7.5,1600,4]

cars = [A1, G2, F3, A2, F2, D4, H2, G1, E4, G3, C4]


i=1
for c in cars:
    print(i,c[1])
    i+=1
    print(" ")

def print_car(c):
    print(c[0], "Car Name:" ,c[1])
    print("|top speed:" , c[2],"             |km/h   0-100 km/h:" , c[5], "seconds|")         
    print("|Horse power:" , c[3],"hp     |Engine size:" , c[6], "ccm         |")
    print("|RPM's:" , c[4],"                |Cylinders:" , c[7],"                 |")


user_car = int(input("Enter car number: "))
print(cars[user_car])


   


