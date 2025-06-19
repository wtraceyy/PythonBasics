#A python program that checks whether a number is even or odd

#A python program that checks whether a letter is a vowel or an alphabet

#A python program that returns the perimeter of a rectangle


#1
number = int(input("Enter a random number:"))

if number % 2 == 0:
     print("The number is even")

else:
     print("The number is odd")

print()

#2
letter=str(input("Enter a random letter:"))

if letter not in "a e i o u":
    print("The letter is not a vowel")

else:
    print("The letter is a consonant")

print()

#3
length = int(input("Enter a certain length:"))
width = int(input("Enter a certain width:"))

perimeter = 2*(length) + 2*(width)

print("The perimeter result is")