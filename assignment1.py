class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0

    def greet(self, other_person):
        print("Hello {0}, I am {1}!".format(other_person.name, self.name))
        self.greeting_count = self.greeting_count + 1

    def print_contact_info(self):
        print(self.name + "'s email: " + self.email + " " + self.name + "'s phone number: " +  self.phone)

    def add_friend(self, other_person):
        return self.friends.append(other_person)

    def num_friends(self):
        return len(self.friends)

    def __repr__(self):
        return "{0} {1} {2}".format(self.name, self.email, self.phone)

sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4984")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")

sonny.greet(jordan)
jordan.greet(sonny)

sonny.print_contact_info()

sonny.add_friend(jordan)

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def print_info(self):
        print(self.make, self.model, self.year)

car = Vehicle("Nissan", "Leaf", "2015")
car.print_info()
