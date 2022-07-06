# Python has many built-in types
# Everything in Python is also considered an object
# int
# float
# str
# list
# set
# dict
# tuple
# range
# bool

# You can define your own types in Python using classes
# and create objects based on those classes

class Runner:

    # __init__() is a type of "dunder" method
    # "dunder" -> Double underscore
    # In particular, the purpose of __init__() is to initially populate values for a Person object that is
    # being initialized
    def __init__(self, first_name, last_name, time):
        self.first_name = first_name
        self.last_name = last_name
        self.time = time
        self.fullname = f"{self.first_name}{self.last_name}"

    # Instance Methods
    def set_go(self):
        print(f"Kay Go {self.fullname}{self.last_name}, you clocked in at {self.time} , on the 400. Great Work")

    # Instance method
    def have_time_trial(self):
        print("Get Ready... our time trial is this friday")
        self.time += 1


# Object creation/instantiation/initialization/construction
# Objects can also be referred to as "instances"
# An "instance of Runner" is the same as a "Runner object"


p1 = Runner("Mark", "Perez", 57)
p2 = Runner("Ayla", "Granados", 63)
p3 = Runner("Daniel", "Cota", 53)

print(type(p1))    # <class '__main__.Person'>
print(type(p2))    # <class '__main__.Person'>
print(type(p3))    # <class '__main__.Person'>

print(p1.first_name)    # Mark
print(p2.first_name)    # Ayla
print(p3.first_name)    # Daniel

print(p1.last_name)    # Perez
print(p2.last_name)    # Granados
print(p3.last_name)    # Cota

print(p1.time)  # 57
print(p2.time)  # 63
print(p3.time)  # 53

p1.set_go()  # self = p1
p2.set_go()  # self = p2
p3.set_go()  # self = p3

p1.have_time_trial()   # self = p1

p1.set_go()  # self = p1
p2.set_go()  # self = p2
p3.set_go()  # self = p3


# You can actually call the instance methods by referring to the class itself (Runner)
# But you still need to provide an object that "self" can refer to
Runner.set_go(p1)
Runner.set_go(p2)
Runner.set_go(p3)

print(p1)
print(p2)
print(p3)

p4 = Runner("Dider", "Sandoval", 63)
print(p4.fullname) # Dider Sandoval
p4.firstname = "Michael"
print(p4.fullname)


class Todo:
    def __init__(self, description):
        self.description = description
        self.completed = False


class User:
    def __init__(self, username, training_log):
        self.username = username
        self.training_log = training_log
        self.todos = []


user1 = User("mperezruns", "400m Time Trial")

todo1 = Todo("Drills")
user1.todos.append(todo1)

user1.todos.append(Todo("Side Lunges"))

print(user1.todos)
print(user1)