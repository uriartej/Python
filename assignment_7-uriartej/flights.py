import datetime
import json

class Flights:
    
    def __init__(self, filename):
        self.filename = filename
        self.data = []
        try:
            with open(self.filename, 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            pass
    
    def write_data(self):
        with open(self.filename, 'w') as f:
            json.dump(self.data, f)
    
    def add_flight(self, origin, destination, number, departure, next_day, arrival):
        if len(departure) != 4 or departure.isnumeric() is False:
            return False
        elif len(arrival) != 4 or arrival.isnumeric() is False:
            return False
        else:
            self.data.append([origin, destination, number, departure, next_day, arrival])
            self.write_data()
            return True
    
    def get_flights(self):
            fts = []
            for x in self.data:
                org = x[0]
                dest = x[1]
                num = x[2]
                dep_hour = x[3][:2]
                dep_min = x[3][2:]
                next_day = x[4]
                arr_hour = x[5][:2]
                arr_min = x[5][2:]
                
                dep = datetime.datetime(1,1,1,int(dep_hour),int(dep_min),0)
                dep_str = dep.strftime('%I').lstrip('0') + ':' + dep.strftime('%M') + dep.strftime('%p').lower()
                
                arr = datetime.datetime(1,1,1,int(arr_hour), int(arr_min), 0)
                arr_str = arr.strftime('%I').lstrip('0') + ':' + arr.strftime('%M') + arr.strftime('%p').lower()
                
                if next_day == 'Y':
                    arr = datetime.datetime(1,1,2,int(arr_hour), int(arr_min), 0)
                    arr_str = '+' + arr.strftime('%I').lstrip('0') + ':' + arr.strftime('%M') + arr.strftime('%p').lower()
                    
                delta = arr - dep
                s = delta.seconds
                hours = s// 3600
                s %= 3600
                minutes = s//60
                dur_str = f'{hours}:{minutes:02}'
                fts.append([org,dest,num,dep_str,arr_str,dur_str])
                return fts
                    