courses = ["Full Stack","Data Science","Cyber Security"]
print(courses)

print()

#accessing an element
print(courses[2])

print()

#looping through an array
for course in courses:
    print(course)

    print()

#adding a new element
courses.append("UI/UX")
print(courses)

print()

#removing an element
courses.remove("Data Science")
print(courses)