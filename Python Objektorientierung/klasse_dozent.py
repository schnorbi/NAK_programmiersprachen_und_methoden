class Lecturer:
    def __init__(self, name, tnumber, pnumber):
        self.__name = name
        self.__tnumber = tnumber
        self.__pnumber = pnumber
        self.__module = []

    def get_name(self):
        return self.__name

    def get_tnumber(self):
        return self.__tnumber

    def set_tnumber(self, tnumber):
        self.__tnumber = tnumber

    def add_module(self, module):
        self.__module.append(module)

    def can_teach(self, module):
        return module in self.__module

lec1 = Lecturer('Daniel', 2345678, 123)
print(lec1.get_tnumber())
lec1.set_tnumber(456789)
lec1.add_module('T121')
print(lec1.can_teach('T121'))
print(lec1.can_teach('T122'))

lec2 = Lecturer('Haase', 2345678, 123)
print(lec2.get_tnumber())
lec2.set_tnumber(456789)
lec2.add_module('T122')
print(lec2.can_teach('T121'))
print(lec2.can_teach('T122'))

class Faculty:
    def __init__(self):
        self.__lecturers = []

    def add_lecturers(self, lecturer):
        self.__lecturers.append(lecturer)

    def find_lecturers(self, module):
        lecturers_can_teach = []
        for lec in self.__lecturers:
            if lec.can_teach(module) == True:
                lecturers_can_teach.append(lec)
        return lecturers_can_teach

fac = Faculty()
fac.add_lecturers(lec1)
for l in fac.find_lecturers('T121'):
    print(l.get_name())