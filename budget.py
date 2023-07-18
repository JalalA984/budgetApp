class Category:

    # Initialize instance variables
    def __init__(self, category):
        self.category = category
        self.ledger = list()
        self.balance = 0

    def __str__(self):
        str = ""
        cat_str_len = len(self.category)
        num_of_stars = 30 - cat_str_len

        # error prone here
        num_of_stars = num_of_stars // 2
        extra = 0
        if not cat_str_len % 2 == 0:
            extra = 1

        str += ("*" * num_of_stars) + self.category +("*" * (num_of_stars + extra)) + "\n"
        for item in self.ledger:
            str += item["description"][:24] + "\n"

        return str


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


#def create_spend_chart(categories):
