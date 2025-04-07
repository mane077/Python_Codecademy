class School:
    def __init__(self, name, level, number):
        self.name = name
        self.level = level
        self.number = number

    def get_name(self):
        return self.name

    def get_level(self):
        return self.level

    def get_number(self):
        return self.number

    def set_number(self, new_number):
        self.number = new_number

    def __repr__(self):
        return f"A {self.level} school named {self.name} with {self.number} students."


a = School("Codecademy", "High", 100)
print(a)
print(a.get_name())
print(a.get_level())
a.set_number(200)
print(a.get_number())


class PrimarySchool(School):
    def __init__(self, name, number, pickup):
        super().__init__(name, 'Primary', number)
        self.pickup = pickup

    def get_pickup(self):
        return self.pickup

    def __repr__(self):
        primaryRepr = super().__repr__()
        return primaryRepr + f'The pickup policy is {self.pickup}'


b = PrimarySchool("Codecademy Primary", 300, "Pickup Allowed")
print(b.get_pickup())
print(b)


class HighSchool(School):
    def __init__(self, name, number, sports):
        super().__init__(name, 'High', number)
        self.sports = sports

    def get_sports(self):
        return self.sports

    def __repr__(self):
        highRepr = super().__repr__()
        return highRepr + f"You can play the following sports: {self.sports}."


c = HighSchool("Codecademy High", 500, ["Tennis", "Basketball"])
print(c.get_sports())
print(c)

