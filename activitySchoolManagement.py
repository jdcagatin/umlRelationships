
class Person():
    def __init__(self, name, __age):
        self.name = name
        self.__age = __age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.__age} years old."

    def get_age(self):
        return self.__age

person1 = Person("Lina", 20)

print(person1.greet())
print(person1.get_age())
#Reflection: Because the `age` attribute is private, it cannot be accessed directly from outside the class. The `age` method provides a way to access the private attribute in a controlled manner.