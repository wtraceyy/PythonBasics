#Program 1
age = int(input("How old are you?"))

if age >= 18:
    print("You are a voter")
else:
    print("You are not a voter")

#Program 2
temperature= float(input("Enter the current temperature e.g 23.0:"))

if temperature > 25.0 :
    print("It is too hot")

elif temperature < 25.0 :
    print("It is too cold")

else:
    print("Normal temperature")

print()

#Program 3
first = int(input("Enter the first number"))
second = int(input("Enter the second number"))
third = int(input("Enter the third number"))

if first > second and first > third :
    print(first,"is the largest number")

elif second > first and second > third:
    print(second,"is the largest number")

else:
    print(third,"is the largest number")

