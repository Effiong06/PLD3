#!/usr/bin/env python3

import json
import datetime
from tabulate import tabulate

# Expense Tracking Functions
def expense_input():
    x = input("Enter cost (e.g., 10.50): $")
    y = input("What did you purchase?: ")
    return x, y

def save_data(expenses_input):
    with open("expenses.json", "w") as f:
        json.dump(expenses_input, f)
    print("Data saved successfully!")

def load_data():
    try:
        with open("expenses.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def display_costs(expenses_input):
    print("\nList of All Costs:")
    for entry in expenses_input.values():
        print(f"${entry['cost']} - {entry['item']}")

def calculate_total(expenses_input):
    total = 0
    for entry in expenses_input.values():
        total += float(entry['cost'])
    return total

# Savings Goal Tracking Classes and Functions

#SavingsGoal class to track a user's savings goals
class SavingsGoal:
    def __init__(self, name, target_amount):
        self.name = name
        self.target_amount = target_amount
        self.current_savings = 0.0
        self.start_date = datetime.date.today()

    def add_savings(self, amount):
        self.current_savings += amount

    def progress_percentage(self):
        return (self.current_savings / self.target_amount) * 100

savings_goals = []

def add_savings_goal():
    name = input("Enter the name of your savings goal: ")
    target_amount = float(input("Enter the target amount: $"))
    goal = SavingsGoal(name, target_amount)
    savings_goals.append(goal)
    print(f"Savings goal '{name}' added with a target of ${target_amount:.2f}.")

def update_savings_progress():
    if not savings_goals:
        print("No savings goals found.")
        return
    print("Select a savings goal to update:")
    for idx, goal in enumerate(savings_goals, start=1):
        print(f"{idx}. {goal.name}")
    choice = int(input("Enter the number of the goal: "))
    if 1 <= choice <= len(savings_goals):
        goal = savings_goals[choice - 1]
        amount = float(input(f"Enter the amount to add to '{goal.name}': $"))
        goal.add_savings(amount)
        print(f"Added ${amount:.2f} to '{goal.name}'. Current savings: ${goal.current_savings:.2f}.")
        print(f"Progress: {goal.progress_percentage():.2f}%")
    else:
        print("Invalid choice.")

def view_savings_goals():
    if not savings_goals:
        print("No savings goals to display.")
        return
    table = []
    for goal in savings_goals:
        table.append([goal.name, f"${goal.target_amount:.2f}", f"${goal.current_savings:.2f}", f"{goal.progress_percentage():.2f}%"])
    headers = ["Goal Name", "Target Amount", "Current Savings", "Progress"]
    print(tabulate(table, headers, tablefmt="grid"))

def delete_savings_goal():
    if not savings_goals:
        print("No savings goals to delete.")
        return
    print("Select a savings goal to delete:")
    for idx, goal in enumerate(savings_goals, start=1):
        print(f"{idx}. {goal.name}")
    choice = int(input("Enter the number of the goal: "))
    if 1 <= choice <= len(savings_goals):
        goal = savings_goals.pop(choice - 1)
        print(f"Savings goal '{goal.name}' deleted.")
    else:
        print("Invalid choice.")

def savings_goal_menu():
    while True:
        print("\nSavings Goal Menu:")
        print("1. Add a new savings goal")
        print("2. Update savings progress")
        print("3. View all savings goals")
        print("4. Delete a savings goal")
        print("5. Return to main menu")
        choice = input("Select an option: ")
        if choice == '1':
            add_savings_goal()
        elif choice == '2':
            update_savings_progress()
        elif choice == '3':
            view_savings_goals()
        elif choice == '4':
            delete_savings_goal()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Main Menu Function to interact with the  user
def main_menu():
    expenses_input = load_data()
    budget = float(input("Enter your initial budget for today: $"))

    while True:
        print("\nMain Menu:")
        print("1. Record an Expense")
        print("2. View All Expenses")
        print("3. View Total Expenses")
        print("4. Savings Goal Tracking")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            x, y = expense_input()
            entry_number = len(expenses_input) + 1
            expenses_input[entry_number] = {"cost": x, "item": y}
            save_data(expenses_input)
        elif choice == '2':
            display_costs(expenses_input)
        elif choice == '3':
            total_expenses = calculate_total(expenses_input)
            print(f"\nYour total expenses for today are: ${total_expenses:.2f}")
            if total_expenses > budget:
                print(f"You have exceeded your budget by: ${total_expenses - budget:.2f}")
            else:
                print(f"You are within your budget! You have ${budget - total_expenses:.2f} remaining.")
        elif choice == '4':
            savings_goal_menu()
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please select a valid option.")
# Run the program
if __name__ == "__main__":
    main_menu()
