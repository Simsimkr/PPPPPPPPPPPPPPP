from basic_clases.basic_seller import Seller
from basic_clases.basic_user import User


class Manager(Seller):
    def __init__(self, data, company):
        super().__init__(data, company)

    def doing(self):
        inp = str(input('1 -- read doc\n'
                        '2 -- read acc\n'
                        'ex -- end session\n'
                        ': '))
        if inp == '1':
            self.reading_doc()
        elif inp == '2':
            self.reading_accs()
        elif inp == 'ex':
            return self.company

    def reading_accs(self):
        accounts = self.reader("accounts")

        while True:
            i = 0
            for el in accounts:
                print(f"{i} -- {el[f'first_name']} {el['last_name']}")
                i += 1
            try:
                inp = input("Choose account to read info: ")
                if inp == 'ex':
                    break
                inp = int(inp)

                us = User(accounts[inp], self.company)
                us.inf()
            except:
                pass

    def reading_doc(self):
        while True:
            print(f"Doc for {self.company.give_data()["day"]}\n"
                  f"ex -- exit")
            inp = input("Choose day to read doc: ")
            if inp == "ex":
                break
            try:
                inp = int(inp) - 1

                inp = str(inp)

                try:
                    with open(f'{inp}.txt', 'r') as xxx:
                        for linijka in xxx:
                            inf = linijka.strip()
                            print(inf)
                except FileNotFoundError:
                    print("Ups! Nie mogę znaleźć pliku. Sprawdź ścieżkę.")
            except:
                print("not day num")
