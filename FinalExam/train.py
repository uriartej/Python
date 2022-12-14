class Train:
    track_gauge = "Standard"

    def __init__(self, color, motor_type):
        self.color = color
        self.motor_type = motor_type
        self.max_cars = 10

class Passenger(Train):
    train_classification = "Passenger"

    def __init__(self, color, motor_type, axel_load):
        super().__init__(color, motor_type)
        self.axel_load = axel_load

class Freight(Train):
    train_classification = "Freight"

    def __init__(self, color, motor_type, axel_load):
        super().__init__(color, motor_type)
        self.axel_load = axel_load

class Metro(Passenger):
    train_type = "Metro"
    chassis_length = 70

class Amtrak(Passenger):
    train_type = "Amtrak"
    chassis_length = 80

class Box(Freight):
    train_type = "Box"
    chassis_length = 90

class Container(Freight):
    train_type = "Container"
    chassis_length = 100