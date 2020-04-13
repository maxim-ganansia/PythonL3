class Vehicle:
    # color = ""
    # electric = bool

    def __init__(self, color, electric):
        self.color = color
        self.electric = electric

    def set_color(self, color_val):
        self.color = color_val

    def set_electric(self, electric_val):
        self.color = electric_val

    def get_color(self):
        return self.color

    def get_electric(self):
        return self.electric


my_vehicle = Vehicle("black", True)
print(my_vehicle.color)


class Bike(Vehicle):
    has_leather = True

    def __init__(self, size, model, leather, color, electric):
        self.size = size
        self.model = model
        self.has_leather = leather
        super().__init__(color, electric)

    def does_bike_have_leather(self):
        return self.has_leather


bike = Bike(100, "Audi", False, "red", True)
print(bike.size)


class Car(Vehicle):
    has_door = True

    def __init__(self, size, model, door, color, electric):
        self.size = size
        self.model = model
        self.has_door = door
        # initialize the parent class
        super().__init__(color, electric)

    def does_car_have_door(self):
        return self.has_door


car = Car("big", "medium", "butterfly", "black", True)
print(car.model)
