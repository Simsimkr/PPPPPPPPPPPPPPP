from basic_clases.basic_seller import Seller
from basic_clases.basic_manager import Manager
from basic_clases.basic_admin import Admin
from basic_clases.basic_user import User
from basic_clases.basic_company import Company

Company.new_day()
company = Company()


def print_account_list():
    accounts = User.reader('accounts')
    i = 0
    for el in accounts:
        print(f"{i} -- {el[f'first_name']} {el['last_name']}")
        i += 1
    return accounts


while True:
    try:
        accounts = print_account_list()
        print("ex - exit")
        inp = input("Choose your account: ")
        if inp == 'ex':
            break
        inp = int(inp)

        try:
            a = accounts[inp]
            for i in range(3):
                in_password = str(input("Insert password: "))

                if in_password == a['password']:
                    if a['position'] == 'admin':
                        user = Admin(accounts[inp], company)
                    elif a['position'] == 'seller':
                        user = Seller(accounts[inp], company)
                    elif a['position'] == 'manager':
                        user = Manager(accounts[inp], company)

                    company = user.doing()
                    print(company)
                    break
                elif in_password == 'ex':
                    break
                else:
                    print("nope")
        except:
            print("fuck")
    except:
        print("not int")

comp = company.give_data()
comp_old = Company.reader()
with open(f'{comp["day"]}.txt', 'w') as text_file:
    text = (f"Dzien: {comp["day"]}\n"
            f"Company balance: was -- {comp_old['all_finans']} -- now: {comp['all_finans']}\n"
            f"Illosc pracownikow: was -- {comp_old['all_pracowniki']} -- now: {comp['all_pracowniki']}\n"
            f"Zakupiono za wszystkie dni:\n")

    for i in range(len(comp["can_buy"][0])):
        text = text + f"\t{comp["can_buy"][0][i]}: {comp["all_bought"][i]}\n"

    text = text + f"Trzeba bylo kupic:\n"

    for i in range(len(comp["can_buy"][0])):
        text = text + f"\t{comp["can_buy"][0][i]}: {comp_old["to_do"]["need"][i]}\n"

    text = text + f"Wszystko zakupiono za dzis:\n"

    for i in range(len(comp["can_buy"][0])):
        text = text + f"\t{comp["can_buy"][0][i]}: {comp["all_bought"][i] - comp_old["all_bought"][i]}\n"

    text = text + f"Zakupiono za dzis:\n"

    if len(comp["to_do"]["orders"]) == 0:
        text = text + f"\tNic nie bylo zamowione\n"
    elif len(comp["to_do"]["orders"]) >= 0:
        for i in range(len(comp["to_do"]["orders"])):
            text = text + f"\tZamuwienie numer {i + 1}\n"
            for a in range(len(comp["can_buy"][0])):
                text = text + f"\t\t{comp["can_buy"][0][a]}: {comp["to_do"]["orders"][i][a]}\n"

    text = text + (f"Zostalo pienezy do zyrzycia: {comp["to_do"]["money_to_use"]}\n"
                   f"Bylo zurzyto: {comp["to_do"]["money_used"]}\n")



    text_file.write(text)

Company.writer(comp)
