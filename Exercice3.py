class vehicle:
    brand = ""
    color = ""
    electric = bool

    def __init__(self, brand, color, electric):
        self.brand = brand
        self.color = color
        self.electric = electric

    def set_brand(self, brand_val):
        self.brand = brand_val

    def set_color(self, color_val):
        self.color = color_val

    def set_electric(self, electric_val):
        self.electric = electric_val

    def get_brand(self):
        return self.brand

    def get_color(self):
        return self.color

    def get_electric(self):
        return self.electric


my_vehicle = vehicle("Peugeot", "black", True)
print(my_vehicle.get_brand(), my_vehicle.get_color(), my_vehicle.get_electric())
