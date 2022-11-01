import json
import calendar

#  1. Create a function named `read_data` which receives a keyword parameter `filename`.
#     1. The function should open the filename in read mode and return a dictionary of the JSON decoded contents of the file.
#     2. If the file does not exist, the function should accept the FileNotFoundError and return an empty dictionary.

def read_data(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    
    
#   1. Create a function named `write_data` which receives a keyword parameter `data` and `filename`
#     1. The function should open the filename in write mode and write the dictionary data into the file encoded as JSON.     
def write_data(data, filename):
    with open(filename, 'w') as f:
        json.dump(data,f)
        
#   1. Create a function named `max_temperature` which receives a keyword parameter `data` and `date`
#     1. The function should return the maximum temperature for all dictionary data where the key contains the date as YYYYMMDD.


def max_temperature(data , date):
    x = 0
    for key in data:
        if date == key[0:8]:
            if date[key]['t'] > x:
                x = data[key]['t']
    return x

#   1. Create a function named `min_temperature` which receives a keyword parameter `data` and `date`
#     1. The function should return the minimum temperature for all dictionary data where the key contains the date as YYYYMMDD.

def min_temperature(data , date):
    x = 9999
    for key in data:
        if date == key[0:8]:
            if date[key]['t'] < x:
                x = data[key]['t']
    return x

#   1. Create a function named `max_humidity` which receives a keyword parameter `data` and `date`
#     1. The function should return the maximum humidity for all dictionary data where the key contains the date as YYYYMMDD.

def max_humidity(data , date):
    x = 0
    for key in data:
        if date == key[0:8]:
            if date[key]['h'] > x:
                x = data[key]['h']
    return x

#   1. Create a function named `min_humidity` which receives a keyword parameter `data` and `date`
#     1. The function should return the minimum humidity for all dictionary data where the key contains the date as YYYYMMDD.


def min_humidity(data , date):
    x = 9999
    for key in data:
        if date == key[0:8]:
            if date[key]['h'] < x:
                x = data[key]['h']
    return x

#   1. Create a function named `tot_rain` which receives a keyword parameter `data` and `date`
#     1. The function should return the sum of rainfall for all dictionary data where the key contains the date as YYYYMMDD.

def tot_rain(data , date):
    x = 0
    for key in data:
        if date == key[0:8]:
            x += data[key]['r']
    return x

#   1. Create a function named `report_daily` which receives a keyword parameter `data` and `date`
#     1. The function should return a single string which when passed to any print function will display on the screen 
#     formatted exactly as indicated in the example output below.  You will most likely be appending strings together 
#     using a literal "\n" where a newline is desired.  To get the month name, you can import the builtin `calendar` 
#     module and call the `month_name` function passing it the month as an integer.

def report_daily (data , date):
    display = "========================= DAILY REPORT ========================\n"
    for key in data:
        if date == key[0:8]:
            m = calendar.month_name[int(date[4:6])] + (date[6:8]), "," + str(int(date[0:4]))
            tm = key[8:10] + ":" + key[10:12] + ":" + key[12:14]
            t = data[key]['t']
            h = data[key]['h']
            r = data[key]['r']
            
            display += f'{m<22}'+ f'{tm<10}'+f'{t>11}'+f'{h>10}'+f'{r>10}' + "\n"
            return display

#   1. Create a function named `report_historical` which receives a keyword parameter `data`
#     1. The function should return a single string which when passed to any print function will 
#        display on the screen formatted exactly as indicated in the example output below.  You will most 
#        likely be appending strings together using a literal "\n" where a newline is desired.  To get the 
#        month name, you can import the builtin `calendar` module and call the `month_name` function passing it 
#        the month as an integer.

        
def report_historical(data):

    display = (
        "============================== HISTORICAL REPORT ===========================\n"
    )
    display = (
        display
        + "                          Minimum      Maximum   Minumum   Maximum     Total\n"
    )
    display = (
        display
        + "Date                  Temperature  Temperature  Humidity  Humidity  Rainfall\n"
    )
    display = (
        display
        + "====================  ===========  ===========  ========  ========  ========\n"
    )

    d = ""
    for key in data:
        if d == key[0:8]:
            continue
        else:
            d = key[0:8]

            m = (
                calendar.month_name[int(d[4:6])]
                + " "
                + str(int(d[6:8]))
                + ", "
                + str(int(d[0:4]))
            )

            min_temp = min_temperature(data=data, date=d)
            max_temp = max_temperature(data=data, date=d)
            min_hum = min_humidity(data=data, date=d)
            max_hum = max_humidity(data=data, date=d)
            rain = tot_rain(data=data, date=d)
            display = (
                display
                + f"{m:20}{min_temp:13}{max_temp:13}{min_hum:10}{max_hum:10}{rain:10.2f}"
                + "\n"
            )

    return display