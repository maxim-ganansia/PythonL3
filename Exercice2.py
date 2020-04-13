class car_lot:
    floors = 0
    total_spots = 0

    def __init__(self, floors, total_spots):
        self.floors = floors
        self.total_spots = total_spots

    def set_floors(self, floors_val):
        self.floors = floors_val

    def set_total_spots(self, total_spots_val):
        self.total_spots = total_spots_val

    def get_floors(self):
        return self.floors

    def get_total_spots(self):
        return self.total_spots


car_lot = car_lot(5, 50)
print(car_lot.get_total_spots())
