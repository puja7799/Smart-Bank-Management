from pathlib import Path
import json
import random
import string

class Bank:
    database = "database.json"
    data = []

    try:
        if Path(database).exists():
            with open(database) as fs:
                data =  json.loads(fs.read())
    except Exception as err:
        print(f"An error occured as {err} try again")

    @classmethod
    def __update(cls):
        with open(cls.database,"w") as fs:
            fs.write(json.dumps(cls.data))
    
    @staticmethod
    def __generate_accountno():
        char = random.choices(string.ascii_uppercase,k = 4)
        digits = random.choices(string.digits,k = 8)
        acc = char + digits
        final = "".join(acc)
        return final

        
    def create_account(self):
        info = {
            "name" : input("Enter your name :- "),
            "age" : int(input("tell your age :- ")),
            "mail" : input("Enter your mail :- "),
            "Balance" : 0,
            "accountno." : Bank.__generate_accountno(),
            "number" : int(input("tell your 10 digit number : "))
        }
        try:
            while True:
                pin = int(input("Enter your 4 digit pin : "))
                if len(str(pin)) != 4:
                    print("your pin must be of 4 digit try again :- ")
                else:
                    info['pin'] = pin
                    break
        except Exception as ValueError:
                print("you can only have numbers try again")
    
        if info['age'] < 18:
             print("you are a minor ")
             return
        else:
            Bank.data.append(info)
            Bank.__update()

    def deposite_money(self):
        acc_no = input("tell your account number:- ")
        pin = int(input("tell your pin :- "))
        user = [i for i in Bank.data if i['pin'] == pin and i['accountno.'] == acc_no]
        if user:
            money = int(input("How much money you want to deposit :- "))
            if money > 100000 or money <= 0:
                print("you cannot deposit more than 100000 rs or less than 0rs")
            else:
                user[0]['Balance'] += money
                print("Money added successfully Thanks visit again 💅")
                Bank.__update()
        else:
            print("Invalid accountno. or pin ")

    def Withdraw_money(self):
        acc_no = input("tell your account number:- ")
        pin = int(input("tell your pin :- "))
        user = [i for i in Bank.data if i['pin'] == pin and i['accountno.'] == acc_no]
        if user:
            money = int(input("How much money you want to withdraw :- "))
            if money > user[0]["Balance"] or money <= 0:
                print("Insufficient Balance 🤣")
            else:
                user[0]['Balance'] -= money
                print("Money debited from your account ")
                Bank.__update()
        else:
            print("Invalid accountno. or pin ")

    def check_details(self):
        acc_no = input("tell your account number:- ")
        pin = int(input("tell your pin :- "))
        user = [i for i in Bank.data if i['pin'] == pin and i['accountno.'] == acc_no]
        if user:
            print("your details are : \n")
            for i in user[0]:
                if i != "pin":
                    print(f"{i} : {user[0][i]}")
        else:
            print("Invalid account no. or pin")
    
    def update_details(self):
        acc_no = input("tell your account number:- ")
        pin = int(input("tell your pin :- "))
        user = [i for i in Bank.data if i['pin'] == pin and i['accountno.'] == acc_no]

        if not user:
            print("invalid number or pin ")
        else:
            newdata = {
                "name" : input("Enter to skip or type your new name : "),
                "mail" : input("Enter to skip or type your new mail : "),
                "number" :input("Enter to skip or type your new number : "),
                "pin":   input("Enter to skip or type your new pin : "),        
            }

            if newdata['name'] == "":
                newdata['name'] = user[0]['name']
            if newdata['mail'] == "":
                newdata['mail'] = user[0]['mail']
            if newdata['number'] == "":
                newdata['number'] = str(user[0]['number'])
            if newdata['pin'] == "":
                newdata['pin'] = str(user[0]['pin'])  
            
            newdata['pin'] = int(newdata['pin'])
            newdata['number'] = int(newdata['number'])

            for i in user[0]:
                if i in newdata:
                    user[0][i] = newdata[i]

            Bank.__update()
            print("Details updated successfully")
    
    def delete_user(self):
        acc_no = input("tell your account number:- ")
        pin = int(input("tell your pin :- "))
        user = [i for i in Bank.data if i['pin'] == pin and i['accountno.'] == acc_no]

        if not user:
             print("invalid number or pin ")
        
        else:
            print("are you sure press y/n")
            check = input("press (y) or (N) ")
            if check == 'y' or check == "Y":
                index = Bank.data.index(user[0])
                Bank.data.pop(index)

                Bank.__update()
                print("Account deleted successfully")
            else:
                print("ok")


bank = Bank()

print("Press 1 for creating an account ")
print("press 2 for depositing money")
print("press 3 for withdrawal")
print("press 4 for checking balance")
print("press 5 for updating some details")
print("press 6 for deactivate your account")
print("press 0 to exit ")

check = int(input("tell your response :- "))


if check == 1:
    bank.create_account()

if check == 2:
    bank.deposite_money()

if check == 3:
    bank.Withdraw_money()

if check == 4:
    bank.check_details()

if check == 5:
    bank.update_details()

if check == 6:
    bank.delete_user()