# This entrypoint file to be used in development. Start by reading README.md
import budget
from budget import create_spend_chart

'''
food = budget.Category("Food")
food.deposit(1000, "initial deposit")
print(food.withdraw(10.15, "groceries"))
print(food.withdraw(15.89, "restaurant and more food for dessert"))
print(food.get_balance())


clothing = budget.Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
print(clothing.withdraw(100))
auto = budget.Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)

print(create_spend_chart([food, clothing, auto]))
'''

'''
# Test toString
food = budget.Category("Food")
entertainment = budget.Category("Entertainment")
business = budget.Category("Business")

food.deposit(900, "deposit")
food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
food.transfer(20, entertainment)
actual = str(food)
expected = f"*************Food*************\ndeposit                 900.00\nmilk, cereal, eggs, bac -45.67\nTransfer to Entertainme -20.00\nTotal: 834.33"

print(repr(expected))
print("================================================")
print(repr(actual))
'''

# Test bar chart
food = budget.Category("Food")
entertainment = budget.Category("Entertainment")
business = budget.Category("Business")

food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
actual = create_spend_chart([business, food, entertainment])
print(repr(actual))
expected = "Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  "
print(repr(expected))
