class Person:
    name = 'Persik'
    surname = 'Sharik'

    def print_inf(self):
        print("Hi,my name is", self.name)
        print("My surname is", self.surname)

person1 = Person()
person1.print_inf()

person2 = Person()
person2.name = "Kirill"
person2.surname = 'Lyzhenkov'
person2.print_inf()