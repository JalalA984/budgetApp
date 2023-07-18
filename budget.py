class Category:

    # Initialize instance variables
    def __init__(self, category):
        self.category = category
        self.ledger = list()
        self.balance = 0

    def __str__(self):
        str_final = ""
        category_str_len = len(self.category)
        num_of_stars = 30 - category_str_len

        # error prone here
        num_of_stars = num_of_stars // 2
        extra = 0
        if not category_str_len % 2 == 0:
            extra = 1

        str_final += ("*" * num_of_stars) + self.category +("*" * (num_of_stars + extra)) + "\n"
        for item in self.ledger:
            right_align_val = 30 - len(item["description"][:24]) - 1
            str_final += item["description"][:23] + " " + f"{item['amount'] : >{right_align_val}}" + "\n"

        return str_final


    # Deposit amount
    def deposit(self, amount, description=""):
        self.ledger.append({"amount" : amount, "description" : description})
        self.balance += amount

    # Withdraw amount if balance allows
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            # There are enough funds to add to ledger
            self.ledger.append({"amount" : -abs(amount), "description" : description})
            self.balance -= amount
        return self.check_funds(amount)

    def get_balance(self):
        return self.balance

    def transfer(self, amount, transfer_category):
        enough_funds = self.withdraw(amount, "Transfer to " + transfer_category.category)
        if enough_funds:
            transfer_category.deposit(amount, "Transfer from " + self.category)
        return enough_funds

    def check_funds(self, amount):
        return amount < self.balance


def create_spend_chart(categories):
    str_final = "Percentage spent by category" + "\n"
    line_100 = "100|"
    line_90 = "90|"
    line_80 = "80|"
    line_70 = "70|"
    line_60 = "60|"
    line_50 = "50|"
    line_40 = "40|"
    line_30 = "30|"
    line_20 = "20|"
    line_10 = "10|"
    line_0 = "0|"
    line_dash = "    ----------"
    str_final += f"{line_100 : >{14}}" + "\n" + f"{line_90 : >{14}}" + "\n" + f"{line_80 : >{14}}" + "\n" +\
                 f"{line_70 : >{14}}" + "\n" + f"{line_60 : >{14}}" + "\n" +f"{line_50 : >{14}}" + "\n" +\
                 f"{line_40 : >{14}}" + "\n" +f"{line_30 : >{14}}" + "\n" +f"{line_20 : >{14}}" +\
                 "\n" +f"{line_10 : >{14}}" + "\n" +f"{line_0 : >{14}}" + "\n" + f"{line_dash : >{14}}"
    return str_final
