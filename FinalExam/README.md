# Exam 3

## Rules of Behavior
1. Do not communicate with anyone during the exam (no email, no social media, no Discord, no texting, no phones, no talking, no passing notes, no internet communicating).  If there is any evidence of communicating with anyone during the exam you will receive a zero.
1. You **must** turn off your cell phone and store it away.
1. Your submission **must** be solely you own work without the assistance of anyone by any means.
1. All programming code **must** be written in Python.
1. You **must** use Tuffix to unit test your program.
1. All your code **must** be submitted on canvas by **12:50 p.m. today**.  Any submissions after that time will not be considered.
1. You may use your book.
1. You may use the Internet as a **reference only**.
1. If you have questions, approach the instructor desk.


## Program Instructions
1. Write several Python classes that perform as a Tuffy Titan Train management module.  You are provided a very simple main.py file that you may use as you are developing your class hierarchies.
1. The class hierarchies should use the following structure:

<p align="center">
  <img src="./exam03b_graphics.png" width="600" title="Hierarchy Diagram">
</p>

1. Create a `train` module to meet the following requirements:
     1. Create a file named `train.py`.
          1. Define a class named `Train`.
               1. Define a class variable (shared by all instances) named `track_gauge` and initialized to the string `Standard`.
               1. Define a member function named `__init__` to meet the following requirements:
                    1. Take a `self` object as a positional parameter.
                    1. Take a `color` string as a keyword parameter.
                    1. Take a `motor_type` string as a keyword parameter.
                    1. Define a `self.color` instance variable initialized to the `color` parameter.
                    1. Define a `self.motor_type` instance variable initialized to the `motor_type` parameter.
                    1. Define a `self.max_cars` instance variable initialized to the integer `10`.

          1. Define a class named `Passenger` which inherits from the `Train` class.
               1. Define a class variable (shared by all instances) named `train_classification` and initialized to the string `Passenger`.
               1. Define a member function named `__init__` to meet the following requirements:
                    1. Take a `self` object as a positional parameter.
                    1. Take a `color` string as a keyword parameter.
                    1. Take a `motor_type` string as a keyword parameter.
                    1. Take a `axel_load` integer as a keyword parameter.
                    1. Call the parent class initialization function and pass the `color` and `motor_type` parameters.
                    1. Define a `self.axel_load` instance variable initialized to the `axel_load` parameter.

          1. Define a class named `Freight` which inherits from the `Train` class.
               1. Define a class variable (shared by all instances) named `train_classification` and initialized to the string `Freight`.
               1. Define a member function named `__init__` to meet the following requirements:
                    1. Take a `self` object as a positional parameter.
                    1. Take a `color` string as a keyword parameter.
                    1. Take a `motor_type` string as a keyword parameter.
                    1. Take a `axel_load` integer as a keyword parameter.
                    1. Call the parent class initialization function and pass the `color` and `motor_type` parameters.
                    1. Define a `self.axel_load` instance variable initialized to the `axel_load` parameter.

          1. Define a class named `Metro` which inherits from the `Passenger` class.
               1. Define a class variable (shared by all instances) named `train_type` and initialized to the string `Metro`.
               1. Define a class variable (shared by all instances) named `chassis_length` and initialized to the integer `70`.

          1. Define a class named `Amtrak` which inherits from the `Passenger` class.
               1. Define a class variable (shared by all instances) named `train_type` and initialized to the string `Amtrak`.
               1. Define a class variable (shared by all instances) named `chassis_length` and initialized to the integer `80`.

          1. Define a class named `Box` which inherits from the `Freight` class.
               1. Define a class variable (shared by all instances) named `train_type` and initialized to the string `Box`.
               1. Define a class variable (shared by all instances) named `chassis_length` and initialized to the integer `90`.

          1. Define a class named `Container` which inherits from the `Freight` class.
               1. Define a class variable (shared by all instances) named `train_type` and initialized to the string `Container`.
               1. Define a class variable (shared by all instances) named `chassis_length` and initialized to the integer `100`.

   Create a main driver program to meet the following requirements:

	Create a file named main.py.
	Import the appointments module.
	create a list which contain all below element inside it
	Element 1 = Metro(axel_load = 9000, motor_type = "Electric", color = "Red")
	Element 2 = Amtrak(axel_load = 10000, motor_type = "Diesel", color = "Black")
	Element 3 = Box(axel_load = 200000, motor_type = "Diesel", color = "Gray")
	Element 4 = Container(axel_load = 160000, motor_type = "Diesel", color = "White")

	and then print the value of the train_classification,train_type,track_gauge, motor_type, color, chassis_length,axel_load,max_cars.

	For box and container you can assign the max_cars values.
1. Run the main.py file as you are developing your model and classes.

    ```
    python3 -m main
    ```

1. Run the unit testing program to ensure that your program runs as expected.

    ```
    ./python3 -m test3
    ```
       
    The unit testing will output the results of a series of tests using specific input and expected output.  Any error will provide information on where the expected output is different from the actual output.  You will need to edit your source code to fix the error and run `./python3 -m test3` repeatedly until it passes all the test.

## Submission


When you completed make a zip folder and uyplad it on canvas.  You should have the following files:
```
train.py
main.py
test.txt
```
    
## Grading
1. All points add up to a total of 100 points possible as detailed below.  Partial credit will be given where applicable.

| Points | Description |
| --- | --- |
|30|initial git clone of this repository to your Tuffix machine|
|15|train.py file submitted contains the appointments module and meets the program requirements|
|10|main.py file submitted contains the appointments module and meets the program requirements|
|10|unit testing test.txt file results submitted|
|2|unit test passes Test01_train_instance_object|
|2|unit test passes Test02_train_class_variable|
|2|unit test passes Test03_passenger_instance_object|
|2|unit test passes Test04_passenger_class_variable|
|2|unit test passes Test05_freight_instance_object|
|5|unit test passes Test06_freight_class_variable|
|5|unit test passes Test07_metro|
|5|unit test passes Test08_amtrak|
|5|unit test passes Test09_box|
|5|unit test passes Test10_container|


