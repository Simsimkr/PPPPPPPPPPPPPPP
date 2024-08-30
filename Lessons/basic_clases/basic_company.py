import json
from random import randint


class Company:
    def __init__(self):
        self.data = Company.reader()

    @staticmethod
    def reader():
        with open(f'company.json', 'r') as json_file:
            date = json.load(json_file)
            return date

    @staticmethod
    def writer(data):
        with open(f'company.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)

    def inf(self):
        print(self.data)

    def to_do_w(self):
        print("TASKs:")
        for i in range(len(self.data["can_buy"][0])):
            print(f"{self.data["can_buy"][0][i]} -- {self.data["to_do"]["need"][i]}")
        print(f'Now balance: {self.data["to_do"]['money_to_use']}')

    @staticmethod
    def new_day():
        data = Company.reader()
        data['day'] += 1
        data["to_do"]['can_give'] = randint(10000, 100000)
        data['all_finans'] = data['all_finans'] - data["to_do"]['can_give']
        print(f'Balance + {data["to_do"]["can_give"]}')
        data["to_do"]['money_to_use'] += data["to_do"]['can_give']
        print(f'Now balance: {data["to_do"]['money_to_use']}')
        data["to_do"]['need'] = [randint(10, 200), randint(50, 500), randint(20, 300)]
        data["to_do"]['orders'] = []
        Company.writer(data)

    def give_data(self):
        return self.data

    def take_data(self, data):
        self.data = data
