import json

class Inventory:
    def __init__(self, filename):
        self.filename = filename
        self.data = {}
        try:
            with open(self.filename, 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            pass
    
    def write_data(self):
        with open(self.filename, 'w') as f:
            json.dump(self.data, f)

    def add_item(self, barcode, description):
        if type(barcode) != str or len(barcode) != 6 or barcode[:2] != "BC" or not barcode[2:].isdigit():
            return 109
        if barcode in self.data:
            return 101
        
        self.data[barcode] = [description, 0]
        self.write_data()
        
        return 100

    def modify_description(self, barcode, description):
        if barcode not in self.data:
            return 102
        
        self.data[barcode] = [description, self.data[barcode][1]]
        self.write_data()
        return 100

    def add_qty(self, barcode, qty):
        if barcode not in self.data:
            return 102
        if type(qty) != int:
            return 108
        self.data[barcode][1] += qty 
        self.write_data()
        return 100

    def remove_qty(self, barcode, qty):
        if barcode not in self.data:
            return 102
        if type(qty) != int:
            return 108
        if qty > self.data[barcode][1]:
            return 103
        self.data[barcode][1] -= qty
        self.write_data()
        return 100 

    def get_inventory(self):
        display = ""
        for (k, v) in self.data.items():
            display += f"{k:8}{v[0]:20}{v[1]:5}\n"

        return display