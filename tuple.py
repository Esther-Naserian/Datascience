#accesing elements in tuples
my_tuples= ("Narok","Nairobi","Migori","Busia","Naivasha")
print(my_tuples)
print(my_tuples[0])
print(my_tuples[1])
print(my_tuples[2])
print(my_tuples[3])
print(my_tuples[4])
#Adding items to tuples
my_numbers =(1,2,3,4)
x= list(my_numbers)
x.append(30)
x.append(60)
my_numbers = tuple(x)
print(x)
#removing items from tuples
my_colors=("pink","red","yellow","green")
y=list(my_colors)
y.remove("pink")
y.remove("green")
my_colors = tuple