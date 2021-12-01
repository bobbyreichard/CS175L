#matplotlib

import matplotlib.pyplot as plt

#main
def main():
    file_name = open('expenses.txt', 'r')
    expenses = file_name.readlines()
    file_name.close

    for i in range(len(expenses)):
        expenses[i] = expenses[i].rstrip('\n')

    slice_labels = ['Rent', 'Gas', 'Food', 'Clothing', 'Car Payment', 'Misc']

    plt.pie(expenses, labels = slice_labels)

    plt.title('Monthly Expenses')

    plt.show()

if __name__=='__main__':
    main()
