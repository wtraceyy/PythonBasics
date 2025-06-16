
number = 45 #Integer
second = 34.98 #Float
greeting = "Hello" #String
IsPythonInteresting = True #Boolean

#Data Structures
fruits = ["apple", "orange", "strawberry"] #This is a list
cars = ("Jeep","BMW","Mercedes") #tuple
countries = {"Kenya","Canada","Brazil"} #set
student = {
    "firstname" : "Tracey",
    "lastname" : "Wanjiku",
    "age" : "17" ,
    "nationality" : "Canadian"
} #Dictionary

print(number)
print(IsPythonInteresting)
print(fruits)
print(cars)
print(countries)
print(student)
print("Nationality:", student["nationality"])


#TypeCasting - Converting one data type to another
print(float(number))
print(int(second))