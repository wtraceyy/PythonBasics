class Student:
    #Properties/Attributes
    name = "Eliud"
    gender = "Male"
    age = 18

    def study(self):
        print("Student is studying")

    def movement(self):
        print("Student is walking")

#creating an object
student1 = Student()
student1.movement()

print(student1.age)

student2 = Student()
print(student2.name)