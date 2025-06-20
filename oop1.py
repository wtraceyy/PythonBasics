class Dog:
    def __init__(self,name,breed,age,color):
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color


    def Sound(self):
        print(self.name,"is barking")

dog1 = Dog("Rex","German shepherd",5,"white")
print(dog1.name)
print(dog1.breed)



dog2 = Dog("Braxton","Siberian Husky",2,"grey")
print(dog2.age)
dog2.Sound()


dog3 = Dog("Milo","Golden Retreiver",3,"brown")
print(dog3.age ,dog3.breed ,dog3.color)



dog4 = Dog("Bosco","Great Dane",2,"black")