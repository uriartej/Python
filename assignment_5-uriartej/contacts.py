from distutils.log import error
import json
class Contacts:

    def __init__(self, filename):
        self.filename = filename
        self.data = {}
        try:
            with open(filename, 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            return{}

    def add_contact(self, id, first_name, last_name):
        exists = id in self.data

        if exists:
            return 'error'

        self.data[id] = [first_name, last_name]
        self.sort_contacts()
        self.write_data()
        return self.data[id]

    def modify_contact(self, id, first_name, last_name):
        exists = id in self.data
        if not exists:
            return 'error'

        self.data[id] = [first_name, last_name]
        self.sort_contacts()
        self.write_data()
        return self.data[id]

    # need to implement steps 3, 4, 5, 6
    def delete_contact(self, id):
        exists = id in self.data
        if not exists:
            return error

        x = self.data.pop(id)
        self.write_data()
        return x


    def write_data(self):
        with open(self.filename, 'w') as f:
            json.dump(self.data, f)

    def sort_contacts(self):
        l = []
        for key in self.data:
            # l.append(key, self.data[key][0].upper(), self.data[key][1].upper(), self.data[key][0], self.data[key][1])
            s = sorted(l, key = lambda x: (x[2], x[1]))

            d = {}

            for items in s:
                id = items[0]
                fn = items[3]
                ln = items[4]

                d[id] = [fn, ln]
                self.data[id] = d
                self.write_data()