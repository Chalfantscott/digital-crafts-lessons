class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def greet(self, other_person):
        print 'Hello %s, I am %s!' % (other_person.name, self.name)

    def print_contact_info(self):
        print "Sonny's email: %s, Sonny's phone number: %s." % (self.email, self.phone)


Sonny = Person("Sonny", "Sonny@hotmail.com", "483-485-4948")
Jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')
Sonny.greet(Jordan)
Jordan.greet(Sonny)

print Sonny.email
print Sonny.phone
print Jordan.email
print Jordan.phone

print Sonny.print_contact_info()