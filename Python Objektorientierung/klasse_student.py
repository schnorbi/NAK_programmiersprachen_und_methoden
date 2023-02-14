class Student:
    def __init__(self, name, matnr):
        self.__name = name
        self.__matnr = matnr
        self.__modules = {}

    def add_module(self, modnr, grade):
        self.__modules[modnr] = grade

    def get_avggrade(self):
        sum = 0
        for mod in self.__modules:
            sum += self.__modules[mod]
        return sum / len(self.__modules)

    def print_gradingtable(self):
        table = f'\nNotenübersicht von {self.__name} Matnr. {self.__matnr} \nModul    Note\n'
        for mod in self.__modules:
            table = f'{table} {mod}     {self.__modules[mod]}\n'
        table = table + f"{'-' * 20} '\nDurchschnittsnote: {self.get_avggrade()}'"
        print(table)


stud1 = Student("Corbian", 193)

stud1.add_module('T121', 3.3)
stud1.add_module('A123', 5.6)
stud1.add_module('G732', 1.0)

print(stud1.get_avggrade())
stud1.print_gradingtable()