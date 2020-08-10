class Dog:
    def __init__(self, name):
        self.name = name
        self.color = "Blue"
        print(self.name,"was Born")
    
    def speak(self):
        print("YELP!", self.name)

    def wag(self):
        print("Dog's wag tail")

    def __del__(self):
        print("destroy!!")

class Puppy(Dog):
    def __init__ (self):
        self.name = "Puppy"
        self.color = "Red"
        print("Puppy was born")
    
    def __read_diary(self):
        print("Diary content!!!!")


    def wag(self):
        self.__read_diary()
        print("Puppy's was tail")

    # def speak(self):
    #     print("Bow wow!")

    # def tto():
    #     print("TtooooooooooooooOOOOOOO")

# class Clac:
#     def plus(a,b):
#         return a + b
d = Dog("Dog")
p = Puppy()
p.speak()


# class Square:
#     def __init__(self, width, Length) :
#         self.width = width
#         self.Length = Length
    
#     def area(self):
#         print("사각형의 넓이는 : {:d}".format(self.width * self.Length))

# class Rec(Square):
#     def __intit__(self, width, Length):
#         self.width = width
#         self.Length = Length

#     def area(self):
#         print("직사각형의 넓이는 : {:d}".format(self.width * self.Length))

# rec = Rec(5,6)
# rec.area()