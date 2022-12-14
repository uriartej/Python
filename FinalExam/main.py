import train

# Create a list of train objects
trains = [
    train.Metro(axel_load = 9000, motor_type = "Electric", color = "Red"),
    train.Amtrak(axel_load = 10000, motor_type = "Diesel", color = "Black"),
    train.Box(axel_load = 200000, motor_type = "Diesel", color = "Gray"),
    train.Container(axel_load = 160000, motor_type = "Diesel", color = "White")
]

# Iterate over the list of trains and print their details
for train in trains:
    print(f"Train classification: {train.train_classification}")
    print(f"Train type: {train.train_type}")
    print(f"Track gauge: {train.track_gauge}")
    print(f"Motor type: {train.motor_type}")
    print(f"Color: {train.color}")
    print(f"Chassis length: {train.chassis_length}")
    print(f"Axel load: {train.axel_load}")
    print(f"Maximum number of cars: {train.max_cars}")