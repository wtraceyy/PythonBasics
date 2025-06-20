#built-in functions/standard library functions
x = max(54 ,78,45,77,67)
print("the maximum number is",x)

y = min(22 , 89, 56, 35, 76)
print("the minimum number is",y)

z = pow(2, 3)
print("the power of 2 is",z)

print()

#user defined functions
def greeting():
    print("Hello world")

greeting() #calling a function

def school():
    print("My coding school is Emobilis")

school()

print()

#Parameter and argument
def add(num1 , num2):
    print(num1 + num2)

add(15,20)
add(22,44)

print()

def student(fullname,course,gender):
    print(fullname,course,gender)

student("Tracey Wanjiku","MIT","Female")
student("Tracey Wanjiku","MIT","Female")
student("Tracey Wanjiku","MIT","Female")
student("Tracey Wanjiku","MIT","Female")


print()


#a python program that displays details of 5 employees at fintech using parameters and arguments
#fullname,email,age,position,salary,marriage status

def career(fullname,course,email,age,position,salary,marriagestatus):
    print(fullname,course,email,age,position,salary,marriagestatus)

career("Tracey Wanjiku","FullStack","wtraceyy@gmail.com","17","Student","25000.05","Single")
career("Mike Wahome","Data Science","mkihumba@gmail.com","24","Spokesperson","25000.05","Single")
career("Mercy Wairimu","MIT","wmercy@gmail.com","35","Treasurer","25000.05","Married")
career("Kelly Atieno","FullStack","katieno@gmail.com","37","Secretary","25000.05","Single")
career("Richard Kamau","CyberSecurity","kamauit@gmail.com","46","Manager","25000.05","Married")