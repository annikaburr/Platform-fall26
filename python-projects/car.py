class Car:

    def __init__(self, color, engine_type, gas_tank, odemeter):
            self.color = color
            self.engine_type = engine_type
            self.gas_tank = gas_tank
            self.odemeter = odemeter

    def __str__(self):
            return f"Color: {self.color}, Engine Type: {self.engine_type}"

    def drive(self):
        if self.engine_type == "4_cylinder":
            gas_tank -= 3
            odemeter += 90
        if self.engine_type == "V8":
            gas_tank -= 4
            odemeter += 50

    def get_gas_tank(self):
        return self.gas_tank()

    def get_odemeter(self):
        return self.odemeter()

    """
    Create three car objects and store them in a list.
    Call the class methods on the first and second cars. The first and second cars are stored
    index 0 and 1 of the list."""
    car_lst = []

    honda = Car("red", "4_cylinder", 10, 0)
    toyota = Car("blue", "V8", 15, 0)
    nissan = Car("green", "4_cylinder", 12, 0)
    car_lst.append(honda)
    car_lst.append(toyota)
    car_lst.append(nissan)

    car_lst[0].drive()
    print(car_lst[0].get_gas_tank())
    print(car_lst[0].get_odemeter())

    car_lst[1].drive()
    print(car_lst[1].get_gas_tank())
    print(car_lst[1].get_odemeter())

   

    
