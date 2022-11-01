from collections import defaultdict
import imp
import math
from msilib import sequence
from random import triangular
from re import A, S
import tarfile
from unittest import result


def number (num):

    if num > 0:
     return "Number is positive"
    elif num == 0:
     return "Number is neutral"
    elif num < 0:
     return "Number is negative"
    else:
     return "Number is not Fit in the given condition"

def score(grade):
    if grade >= 90:
        return "Congrats! you scored grade A ..."
    elif grade >= 80:
        return "You scored grade B..."
    elif grade >= 70:
        return "You scored grade C..."
    elif grade >= 60:
        return "You scored grade D..."
    else:
        return "Sorry you fail ?"

def rollcall(student_name):
    records = {'Mayur': 90, 'Peter': 100, 'Sam':50}

    for name in records:
        if name == student_name:
              return records[name]
        break
    else:
        return "Student does not exist"

from collections import defaultdict

nums = [3,2,4]
target = 7
def twonums(nums: list[int], target: int):
    number = defaultdict(int)

    for i ,n in enumerate(nums):
        if target - n in number:
            return [i, number[target - n]]
        number [n] = i


sequence = {"Python", "Java", "Statement"}
for value in sequence:
    if value == "Java":
        pass
    else:
        print('Havent reached to Java: ' , value)

def twoSum(nums: list[int], target: int):
        for i in range(len(nums)):
            for j in range(i + 1, lens(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]


def area_of_triangle(a, b, c):
    s = a + b + c / 2
    area = math.sqrt ((s * (s-a) * (s-b) * (s-c)))
    print (area)

def area_of_circle(a):
    pie = 3.146
    s = a * a * pie
    print (s)

def area_of_square(a):
    s = a * a
    print (s)

def area_of_rectangle(a, b):
    s = a * b
    print (s)