import sqlite3
import matplotlib.pyplot as plt
import csv

# Connect to SQLite database
conn = sqlite3.connect('expenses.db')
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY,
    amount REAL,
    category TEXT,
    date TEXT
)
''')
conn.commit()

# Function to add an expense
def add_expense(amount, category, date):
    cursor.execute('INSERT INTO expenses (amount, category, date) VALUES (?, ?, ?)',
                   (amount, category, date))
    conn.commit()

# Function to show all expenses
def show_expenses():
    cursor.execute('SELECT * FROM expenses')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# Function to export to CSV
def export_to_csv(filename='expenses.csv'):
    cursor.execute('SELECT * FROM expenses')
    rows = cursor.fetchall()
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['ID', 'Amount', 'Category', 'Date'])
        csvwriter.writerows(rows)
    print(f'Expenses exported to {filename}')

# Function to plot expenses by category
def plot_expenses_by_category():
    cursor.execute('SELECT category, SUM(amount) FROM expenses GROUP BY category')
    data = cursor.fetchall()
    categories = [row[0] for row in data]
    amounts = [row[1] for row in data]

    plt.bar(categories, amounts)
    plt.xlabel('Category')
    plt.ylabel('Total Amount')
    plt.title('Expenses by Category')
    plt.show()

# Simple CLI interface
def main():
    while True:
        print("\n1. Add Expense\n2. Show Expenses\n3. Export to CSV\n4. Plot Expenses by Category\n5. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            date = input("Enter date (YYYY-MM-DD): ")
            add_expense(amount, category, date)
        elif choice == '2':
            show_expenses()
        elif choice == '3':
            export_to_csv()
        elif choice == '4':
            plot_expenses_by_category()
        elif choice == '5':
            break
        else:
            print("Invalid option. Please try again.")

    conn.close()

if __name__ == "__main__":
    main()
