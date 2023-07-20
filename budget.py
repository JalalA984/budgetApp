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
        else:
            line_0 += "   "
        if category_spent[cgory] >= 10:
            line_10 += "o  "
        else:
            line_10 += "   "
        if category_spent[cgory] >= 20:
            line_20 += "o  "
        else:
            line_20 += "   "
        if category_spent[cgory] >= 30:
            line_30 += "o  "
        else:
            line_30 += "   "
        if category_spent[cgory] >= 40:
            line_40 += "o  "
        else:
            line_40 += "   "
        if category_spent[cgory] >= 50:
            line_50 += "o  "
        else:
            line_50 += "   "
        if category_spent[cgory] >= 60:
            line_60 += "o  "
        else:
            line_60 += "   "
        if category_spent[cgory] >= 70:
            line_70 += "o  "
        else:
            line_70 += "   "
        if category_spent[cgory] >= 80:
            line_80 += "o  "
        else:
            line_80 += "   "
        if category_spent[cgory] >= 90:
            line_90 += "o  "
        else:
            line_90 += "   "
        if category_spent[cgory] >= 100:
            line_100 += "o  "
        else:
            line_100 += "   "

    # Find longest category name
    longest_str = ""
    for cgory in category_spent:
        if len(cgory) > len(longest_str):
            longest_str = cgory

    num_of_letter_lines = list()
    for x in range(len(longest_str)):
        num_of_letter_lines.append("     ")


    for cgory in category_spent:
        idx = 0
        for _ in range(len(longest_str)):
            try:
                num_of_letter_lines[idx] += cgory[idx] + "  "
                idx += 1
            except:
                curr_idx = idx
                for _ in range(len(longest_str) - idx):
                    num_of_letter_lines[curr_idx] += "   "
                    curr_idx += 1
                break

    str_final += line_100 + "\n" + line_90 + "\n" + line_80 + "\n" + line_70 + "\n" + line_60 + "\n" + line_50 + "\n"\
                 + line_40 + "\n" + line_30 + "\n" + line_20 + "\n" + line_10 + "\n" + line_0 + "\n" + line_dash + "\n"

    for line in num_of_letter_lines:
        if line != num_of_letter_lines[-1]:
            str_final += line + "\n"
        else:
            str_final += line

    return str_final
