class Student:

    def __init__(self, fname, lname, id, energy_level=10):
        self.fname = fname
        self.lname = lname
        self.id = id
        self.energy_level = energy_level

    def __str__(self):
        return f" {lname} : {id}"

    def greeting(self):


    def take_exam(self, energy_level):
        updated_energy_level = energy_level - 1

    def get_energy_level(self, updated_energy_level):
        return updated_energy_level

    