# class Address:
#     def __init__(self):
#         self.street = "1200 Richmond Ave"
#         self.city = "Houston"
#         self.state = "TX"
#
#
#
# class User:
#     def __init__(self,firstName,lastName):
#         self.firstName = firstName
#         self.lastName = lastName
#         self.addresses = []
#
#
#
# john_doe = User("John","Doe")
# address1 = Address()
# address2 = Address()
#
# john_doe.addresses.append(address1)
# john_doe.addresses.append(address2)
#
#
# print(john_doe.addresses)
#

class Battery:
    def __init__(self,life,manufacturer):
        self.life = life
        self.manufacturer = manufacturer

    def __repr__(self):
        return "Life = {0}, Manufacturer = {1}".format(self.life, self.manufacturer)



class Electric_car:
    def __init__(self,make,model,battery):
        self.make = make
        self.model = model
        self.battery = battery

    def pretty_print(self):
        print("Make = {0}, Model = {1}".format(self.make, self.model))
        print(self.battery)

battery = Battery(100, "CC")
car = Electric_car("Tesla", "Model X", battery)

car.pretty_print()
