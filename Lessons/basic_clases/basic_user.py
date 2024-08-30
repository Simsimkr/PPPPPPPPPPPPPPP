import json

class User:
    def __init__(self, data,  company):
        self.data = data
        self.company = company

    def inf(self):
        for k, v in self.data.items():
            print(f'{k} -- {v}')

    @staticmethod
    def reader(wtr: str):
        with open(f'{wtr}.json', 'r') as json_file:
            date = json.load(json_file)
            return date

    @staticmethod
    def writer(wtr, data):
        with open(f'{wtr}.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)
