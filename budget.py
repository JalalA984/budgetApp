from collections import OrderedDict
from math import floor


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
        total = 0
        for item in self.ledger:
            right_align_val = 30 - len(item["description"][:24]) - 1
            str_final += item["description"][:23] + " " + f"{format(item['amount'], '.2f') : >{right_align_val}}" + "\n"
            total += item["amount"]

        str_final += "Total: " + str(total)
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
        if amount > self.balance:
            return False
        else:
            return True


def create_spend_chart(categories):
    # Calculate overall percentage spent for each category in list
    overall_spent = 0
    category_spent = dict()
    for cgory in categories:
        for item in cgory.ledger:
            if item["amount"] < 0:
                overall_spent += abs(item["amount"])
                category_spent[cgory.category] = category_spent.get(cgory.category,0) + abs(item["amount"])

    category_spent = OrderedDict((list(category_spent.items())))

    for cgory in category_spent:
        # Update dictionary values to percentages and round down to nearest tenth
        category_spent[cgory] = floor(((category_spent[cgory] / overall_spent) * 100) / 10) * 10

    # Calculate dashes for x-axis
    number_of_dashes = 0
    for cgory in category_spent:
        number_of_dashes += 3
    if number_of_dashes != 0:
        number_of_dashes += 1
    line_dash = "    "
    for _ in range(number_of_dashes):
        line_dash += "-"

    # Define constants needed for formatting
    overall_width = len(line_dash)

    str_final = "Percentage spent by category" + "\n"
    line_100 = "100| "
    line_90 = " 90| "
    line_80 = " 80| "
    line_70 = " 70| "
    line_60 = " 60| "
    line_50 = " 50| "
    line_40 = " 40| "
    line_30 = " 30| "
    line_20 = " 20| "
    line_10 = " 10| "
    line_0 = "  0| "

    for cgory in category_spent:
        if category_spent[cgory] >= 0:
            line_0 += "o  "
        if category_spent[cgory] >= 10:
            line_10 += "o  "
        if category_spent[cgory] >= 20:
            line_20 += "o  "
        if category_spent[cgory] >= 30:
            line_30 += "o  "
        if category_spent[cgory] >= 40:
            line_40 += "o  "
        if category_spent[cgory] >= 50:
            line_50 += "o  "
        if category_spent[cgory] >= 60:
            line_60 += "o  "
        if category_spent[cgory] >= 70:
            line_70 += "o  "
        if category_spent[cgory] >= 80:
            line_80 += "o  "
        if category_spent[cgory] >= 90:
            line_90 += "o  "
        if category_spent[cgory] >= 100:
            line_100 += "o  "





    str_final += f"{line_100 : <{overall_width}}" + "\n" + f"{line_90 : <{overall_width}}" + "\n" + f"{line_80 : <{overall_width}}" + "\n" +\
                 f"{line_70 : <{overall_width}}" + "\n" + f"{line_60 : <{overall_width}}" + "\n" +f"{line_50 : <{overall_width}}" + "\n" +\
                 f"{line_40 : <{overall_width}}" + "\n" +f"{line_30 : <{overall_width}}" + "\n" +f"{line_20 : <{overall_width}}" +\
                 "\n" +f"{line_10 : <{overall_width}}" + "\n" +f"{line_0 : <{overall_width}}" + "\n" + f"{line_dash : <{overall_width}}"
    return str_final
