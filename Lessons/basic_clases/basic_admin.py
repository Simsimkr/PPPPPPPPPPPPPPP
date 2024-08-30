import uuid

from basic_clases.basic_user import User


class Admin(User):
    def __init__(self, data, company):
        super().__init__(data, company)

    def doing(self):
        while True:
            inp = str(input('1 -- redact an account\n'
                            '2 -- create new account\n'
                            '3 -- delete someones account\n'
                            'ex -- end session\n'
                            ': '))
            if inp == '1':
                self.redact()
            elif inp == "2":
                self.create_account()
            elif inp == "3":
                self.delete_account()
            elif inp == 'ex':
                return self.company

    def delete_account(self):
        accounts = User.reader('accounts')

        while True:
            i = 0
            for el in accounts:
                print(f"{i} -- {el[f'first_name']} {el['last_name']}")
                i += 1
            try:
                inp = input("Choose account to delete: ")
                if inp == 'ex':
                    break
                inp = int(inp)

                while True:
                    us = User(accounts[inp], self.company)
                    us.inf()
                    a = input("Want to delete THIS account?: ")
                    if a == 'yes':
                        accounts.remove(accounts[inp])
                        comp = self.company.give_data
                        comp["all_pracowniki"] = comp["all_pracowniki"] - 1
                        self.company.take_data(comp)
                        User.writer("accounts", accounts)
                        break
                    elif a == "no":
                        break
                    else:
                        pass
            except:
                pass

    def create_account(self):
        accounts = User.reader("accounts")

        while True:
            f_name = str(input('Input first name: '))
            if f_name == 'ex':
                break
            l_name = str(input('Input last name: '))
            if l_name == "ex":
                break
            while True:
                try:
                    age = input('Input age: ')
                    age = int(age)
                    break
                except:
                    if age == "ex":
                        break
                    else:
                        print("not int")
            if age == 'ex':
                break

            while True:
                pos = self.company.give_data()['positions']
                for el in pos:
                    print(f'{pos.index(el)} -- {el}')
                try:
                    inp = int(input("Input position number: "))
                    position = pos[inp]
                    break
                except:
                    if inp == "ex":
                        break
                    else:
                        print("not int")
            if inp == 'ex':
                break

            passwors = str(input("Input password: "))

            acc = {
                "first_name": f_name,
                "last_name": l_name,
                "age": age,
                "position": position,
                "password": passwors,
                "id": str(uuid.uuid4())
            }

            for k, v in acc.items():
                print(f"{k} -- {v}")

            while True:
                inp = str(input("create (c) or destroy (d): "))
                if inp == 'c':
                    accounts.append(acc)
                    User.writer('accounts', accounts)
                    ac = self.company.give_data()
                    ac['all_pracowniki'] = len(accounts)
                    self.company.take_data(ac)
                    break
                elif inp == 'd':
                    break
            break

    def redact(self):
        accounts = User.reader("accounts")
        ok = False
        while not ok:
            try:
                i = 0
                for el in accounts:
                    print(f"{i} -- {el[f'first_name']} {el['last_name']}")
                    i += 1
                num_acc = input("Choose account: ")
                if num_acc == 'ex':
                    break
                num_acc = int(num_acc)
                try:
                    acc = accounts[num_acc]
                    ok = True
                except:
                    print("fuck")
            except:
                print("not int")
        while ok:
            for k, v in acc.items():
                print(f"{k} -- {v}")
            try:
                inp = input('To change: ')
                if inp == 'ex':
                    break
                a = acc[inp]
                acc[inp] = input("New date: ")
                for k, v in acc.items():
                    print(f"{k} -- {v}")
                ask = input("it is all to change?\n"
                            ": ")
                if ask.lower() == 'yes':
                    accounts[num_acc] = acc
                    User.writer('accounts', accounts)
                    ok = False
            except:
                print("dood")
