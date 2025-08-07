#typecasting it means converting one data type to another data type
# but the smalller data type covert into bigger data type to prevent data loss


#EXPLICIT TYPECASTING  - COVERT BY THE USER

a =34
b = "45"
c=int(b)
print(a+c)
print(type(a+c))




#IMPLICIT TYPECASTING - CONVERT BY THE COMPILER its OWN
#INT TO FLOAT

a = 34.56
b = 45
print(a+b)
print(type(a+b))