class User:
    def __init__(self, first, last, age):
        self.first=first
        self.last=last
        self.age=age
        
    def full_name(self):
        return f"{self.first} {self.last}"
    
    def initials(self):
        return f"{self.first[0]}. {self.last[0]}."
        
        
user1 = User("Joe", "Smith", 37)
user2 = User("Blanca", "Lopez", 32)

print(user1.first, user1.last)
print(user2.age)
print(user2.full_name())
print(user2.full_name())
print(user1.initials())