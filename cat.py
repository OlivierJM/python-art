# cat module

class Cat: 
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(self.name, "says Meoww")

    def drink(self):
        print(self.name, "drink some")