import unittest
import io

from train import *

class Test01_train_instance_object(unittest.TestCase):
    def test_list_int(self):
        obj = Train(motor_type="Electric",color="Green")
        self.assertEqual(obj.motor_type, "Electric")
        self.assertEqual(obj.color, "Green")
        self.assertEqual(obj.max_cars, 10)
        self.assertEqual(obj.track_gauge, "Standard")
        print()

class Test02_train_class_variable(unittest.TestCase):
    def test_list_int(self):
        obj1 = Train(motor_type="Electric",color="Green")
        obj2 = Train(motor_type="Diesel",color="Red")
        Train.track_gauge = "Narrow"
        obj1.color = "Blue"
        self.assertEqual(obj1.color, "Blue")
        self.assertEqual(obj2.color, "Red")
        self.assertEqual(obj1.track_gauge, "Narrow")
        self.assertEqual(obj2.track_gauge, "Narrow")
        Train.track_gauge = "Standard"
        print()

class Test03_passenger_instance_object(unittest.TestCase):
    def test_list_int(self):
        obj = Passenger(axel_load=25000, motor_type="Diesel",color="Orange")
        self.assertEqual(obj.motor_type, "Diesel")
        self.assertEqual(obj.color, "Orange")
        self.assertEqual(obj.max_cars, 10)
        self.assertEqual(obj.track_gauge, "Standard")
        self.assertEqual(obj.axel_load, 25000)
        print()

class Test04_passenger_class_variable(unittest.TestCase):
    def test_list_int(self):
        obj1 = Passenger(axel_load=25000, motor_type="Diesel",color="Black")
        obj2 = Passenger(axel_load=50000, motor_type="Electric",color="Green")
        Passenger.train_classification = "Passenger Passenger"
        obj1.axel_load = 30000
        self.assertEqual(obj1.axel_load, 30000)
        self.assertEqual(obj2.axel_load, 50000)
        self.assertEqual(obj1.train_classification, "Passenger Passenger")
        self.assertEqual(obj2.train_classification, "Passenger Passenger")
        Passenger.train_classification = "Passenger"
        print()

class Test05_freight_instance_object(unittest.TestCase):
    def test_list_int(self):
        obj = Freight(axel_load=95000, motor_type="Diesel",color="Gray")
        self.assertEqual(obj.motor_type, "Diesel")
        self.assertEqual(obj.color, "Gray")
        self.assertEqual(obj.max_cars, 10)
        self.assertEqual(obj.track_gauge, "Standard")
        self.assertEqual(obj.axel_load, 95000)
        print()

class Test06_freight_class_variable(unittest.TestCase):
    def test_list_int(self):
        obj1 = Freight(axel_load=95000, motor_type="Diesel",color="Gray")
        obj2 = Freight(axel_load=100000, motor_type="Gas",color="Black")
        Freight.train_classification = "Heavy Freight"
        obj1.axel_load = 90000
        self.assertEqual(obj1.axel_load, 90000)
        self.assertEqual(obj2.axel_load, 100000)
        self.assertEqual(obj1.train_classification, "Heavy Freight")
        self.assertEqual(obj2.train_classification, "Heavy Freight")
        Freight.train_classification = "Freight"
        print()

class Test07_metro(unittest.TestCase):
    def test_list_int(self):
        obj1 = Metro(axel_load=35000, motor_type="Gas",color="Red")
        obj2 = Metro(axel_load=50000, motor_type="Electric",color="Green")
        obj1.motor_type = "Diesel"
        obj2.axel_load = 45000
        Passenger.train_classification = "Passenger Passenger"
        Passenger.track_gauge = "Narrow"
        Freight.train_classification = "Heavy Freight"
        self.assertEqual(obj1.train_classification, "Passenger Passenger")
        self.assertEqual(obj1.train_type, "Metro")
        self.assertEqual(obj1.track_gauge, "Narrow")
        self.assertEqual(obj1.motor_type, "Diesel")
        self.assertEqual(obj1.color, "Red")
        self.assertEqual(obj1.chassis_length, 70)
        self.assertEqual(obj1.axel_load, 35000)
        self.assertEqual(obj1.max_cars, 10)
        self.assertEqual(obj2.train_classification, "Passenger Passenger")
        self.assertEqual(obj2.train_type, "Metro")
        self.assertEqual(obj2.track_gauge, "Narrow")
        self.assertEqual(obj2.motor_type, "Electric")
        self.assertEqual(obj2.color, "Green")
        self.assertEqual(obj2.chassis_length, 70)
        self.assertEqual(obj2.axel_load, 45000)
        self.assertEqual(obj2.max_cars, 10)
        Passenger.train_classification = "Passenger"
        Passenger.track_gauge = "Standard"
        Freight.train_classification = "Freight"
        print()

class Test08_amtrak(unittest.TestCase):
    def test_list_int(self):
        obj1 = Amtrak(axel_load=35000, motor_type="Gas",color="Red")
        obj2 = Amtrak(axel_load=50000, motor_type="Electric",color="Green")
        obj1.motor_type = "Diesel"
        obj2.axel_load = 45000
        Passenger.train_classification = "Passenger Passenger"
        Passenger.track_gauge = "Narrow"
        Freight.train_classification = "Heavy Freight"
        self.assertEqual(obj1.train_classification, "Passenger Passenger")
        self.assertEqual(obj1.train_type, "Amtrak")
        self.assertEqual(obj1.track_gauge, "Narrow")
        self.assertEqual(obj1.motor_type, "Diesel")
        self.assertEqual(obj1.color, "Red")
        self.assertEqual(obj1.chassis_length, 80)
        self.assertEqual(obj1.axel_load, 35000)
        self.assertEqual(obj1.max_cars, 10)
        self.assertEqual(obj2.train_classification, "Passenger Passenger")
        self.assertEqual(obj2.train_type, "Amtrak")
        self.assertEqual(obj2.track_gauge, "Narrow")
        self.assertEqual(obj2.motor_type, "Electric")
        self.assertEqual(obj2.color, "Green")
        self.assertEqual(obj2.chassis_length, 80)
        self.assertEqual(obj2.axel_load, 45000)
        self.assertEqual(obj2.max_cars, 10)
        Passenger.train_classification = "Passenger"
        Passenger.track_gauge = "Standard"
        Freight.train_classification = "Freight"
        print()

class Test09_box(unittest.TestCase):
    def test_list_int(self):
        obj1 = Box(axel_load=200000, motor_type="Gas",color="Black")
        obj2 = Box(axel_load=180000, motor_type="Electric",color="Red")
        obj1.motor_type = "Diesel"
        obj2.axel_load = 190000
        obj2.max_cars = 100
        Freight.train_classification = "Heavy Freight"
        Freight.track_gauge = "Wide"
        Passenger.train_classification = "Passenger Passenger"
        Box.chassis_length = 120
        self.assertEqual(obj1.train_classification, "Heavy Freight")
        self.assertEqual(obj1.train_type, "Box")
        self.assertEqual(obj1.track_gauge, "Wide")
        self.assertEqual(obj1.motor_type, "Diesel")
        self.assertEqual(obj1.color, "Black")
        self.assertEqual(obj1.chassis_length, 120)
        self.assertEqual(obj1.axel_load, 200000)
        self.assertEqual(obj1.max_cars, 10)
        self.assertEqual(obj2.train_classification, "Heavy Freight")
        self.assertEqual(obj2.train_type, "Box")
        self.assertEqual(obj2.track_gauge, "Wide")
        self.assertEqual(obj2.motor_type, "Electric")
        self.assertEqual(obj2.color, "Red")
        self.assertEqual(obj2.chassis_length, 120)
        self.assertEqual(obj2.axel_load, 190000)
        self.assertEqual(obj2.max_cars, 100)
        Freight.train_classification = "Freight"
        Freight.track_gauge = "Standard"
        Passenger.train_classification = "Passenger"
        Box.chassis_length = 90
        print()

class Test10_container(unittest.TestCase):
    def test_list_int(self):
        obj1 = Container(axel_load=200000, motor_type="Gas",color="Black")
        obj2 = Container(axel_load=180000, motor_type="Electric",color="Red")
        obj1.motor_type = "Diesel"
        obj2.axel_load = 190000
        obj2.max_cars = 100
        Freight.train_classification = "Heavy Freight"
        Freight.track_gauge = "Wide"
        Passenger.train_classification = "Passenger Passenger"
        Container.chassis_length = 120
        self.assertEqual(obj1.train_classification, "Heavy Freight")
        self.assertEqual(obj1.train_type, "Container")
        self.assertEqual(obj1.track_gauge, "Wide")
        self.assertEqual(obj1.motor_type, "Diesel")
        self.assertEqual(obj1.color, "Black")
        self.assertEqual(obj1.chassis_length, 120)
        self.assertEqual(obj1.axel_load, 200000)
        self.assertEqual(obj1.max_cars, 10)
        self.assertEqual(obj2.train_classification, "Heavy Freight")
        self.assertEqual(obj2.train_type, "Container")
        self.assertEqual(obj2.track_gauge, "Wide")
        self.assertEqual(obj2.motor_type, "Electric")
        self.assertEqual(obj2.color, "Red")
        self.assertEqual(obj2.chassis_length, 120)
        self.assertEqual(obj2.axel_load, 190000)
        self.assertEqual(obj2.max_cars, 100)
        Freight.train_classification = "Freight"
        Freight.track_gauge = "Standard"
        Passenger.train_classification = "Passenger"
        Container.chassis_length = 90
        print()

if __name__ == '__main__':
    with open('test.txt', "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
