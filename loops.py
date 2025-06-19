# While loop
number = 20

while number <= 25 :
    print(number)
    number += 1

print()

    #Decrementing
count = 105

while count >= 100 :
    print(count)
    count -= 1

print()

#Break and Continue
a = 20
while a <= 25 :
    print(a)
    if a == 23:
        break
    a +=  1

print()

b = 35
while b <= 40 :
    if b == 37:
        b += 1
        continue
    print(b)
    b += 1



print()

#For loop
languages = ["Python" , "C++" , "Java", "PHP"]
for lang in languages:
    print(lang)

print()

for num in range(5):
    print(num)

print()

for x in range(10 , 15):
    print(x)

print()

for z in range(10, 20 ,3):
    print(z)