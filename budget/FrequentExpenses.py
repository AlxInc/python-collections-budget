from . import Expense
import collections
import matplotlib.pyplot as plt

expenses = Expense.Expenses()

expenses(read_expenses(data/spending_data.csv))

spending_categories = []
for expense in expenses.list:
    spending_categories.append(expense.category)

spending_counter = collections.Counter(spending_categories)

def spending_counter(most_common):
    top5 = most_common(5)
    return top5

categories,count = zip(*top5)
fig, ax = plt.subplots()

ax.bar(categories, count)
ax.set_title(str: '# of Purchases by Category')

plt.show()