

class Dog:
    species = "Canis familiaris"
    def __init__(self, name, age):
        self.name = name
        self.age = age
        

    def description(self):
        return f"{self.name} is {self.age} years old"
    
    def speak(self, sound):
        return f"{self.name} barks: {sound}"
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass

class GoldenRetriever(Dog):
    def speak(self, sound="Bark"):
        return f"{self.name} says {sound}"

miles = JackRussellTerrier("Miles", 4 )
buddy = Dachshund("Buddy", 9 )
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)
luna = GoldenRetriever("Luna", 3)


print(buddy.speak("yap"))
print(miles.speak())
print(luna.speak())