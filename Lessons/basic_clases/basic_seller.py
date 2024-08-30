from basic_clases.basic_user import User


class Seller(User):
    def __init__(self, data, company):
        super().__init__(data, company)

    def doing(self):
        while True:
            inp = str(input('1 -- work\n'
                            'ex -- end session\n'
                            ': '))
            if inp == '1':
                self.work()
            elif inp == 'ex':
                return self.company

    def work(self):
        comp_data = self.company.give_data()

        order = [0, 0, 0]
        while True:
            while True:
                all_cost = 0
                self.company.to_do_w()
                for i in range(len(comp_data["can_buy"][0])):
                    print(f"Ordered {comp_data["can_buy"][0][i]} -- {order[i]} -- cost: {comp_data["can_buy"][1][i] * order[i]} -- cena: {comp_data["can_buy"][1][i]}")
                    all_cost += comp_data["can_buy"][1][i] * order[i]
                print(f"All cost: {all_cost}")
                print(f"Money left: {comp_data["to_do"]["money_to_use"] - all_cost} ")

                inp = str(input("What want buy? :")).lower()
                if inp == "ex":
                    break

                while True:
                    try:
                        for i in range(len(comp_data["can_buy"][0])):
                            if inp == comp_data["can_buy"][0][i]:
                                print(f"Want to Buy {comp_data["can_buy"][0][i]} -- cena: {comp_data["can_buy"][1][i]}")

                                while True:
                                    count = input(f"Please input how much? (need: {comp_data['to_do']["need"][i]}) : ")
                                    if count == "ex":
                                        break
                                    else:
                                        count = int(count)

                                    if count > comp_data["to_do"]["need"][i]:
                                        print("Izia! Po co tyle?!")
                                    elif count <= comp_data["to_do"]["need"][i]:
                                        if count * comp_data["can_buy"][1][i] > comp_data["to_do"]['money_to_use']:
                                            print("NO ENOUGH MONEY")
                                        else:
                                            order[i] = count
                                            break
                                if count == "ex":
                                    break
                        break

                    except:
                        print("not int")

            while True:
                print("It is all?")
                a = input(":")
                if a.lower() == "yes" or a.lower() == "no":
                    break
                else:
                    pass

            if a == "yes":
                acc = self.company.give_data()
                acc["to_do"]["orders"].append(order)
                acc["to_do"]["money_used"] = all_cost
                acc["to_do"]["money_to_use"] = comp_data["to_do"]["money_to_use"] - acc["to_do"]["money_used"]
                for i in range(len(acc["can_buy"][0])):
                    acc["all_bought"][0] += order[i]
                    acc["to_do"]["need"][i] -= order[i]

                self.company.take_data(acc)
                break




