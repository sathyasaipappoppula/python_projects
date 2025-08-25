from datetime import datetime

# ------------------ Expense Class ------------------
class Expense:
    def __init__(self, amount, category, description=""):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f"Amount: ₹{self.amount} | Category: {self.category} | Date: {self.date} | Note: {self.description}"

# ------------------ ExpenseTracker Class ------------------
class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.next_id = 1

    def add_expense(self, expense: Expense):
        self.expenses.append((self.next_id, expense))
        self.next_id += 1
        print("✅ Expense added successfully!")

    def view_expenses(self):
        if not self.expenses:
            print("⚠️ No expenses recorded yet.")
            return

        print("\n---- All Expenses ----")
        for exp_id, expense in self.expenses:
            print(f"ID: {exp_id} | {expense}")

    def delete_expense(self, expense_id):
        for i, (exp_id, expense) in enumerate(self.expenses):
            if exp_id == expense_id:
                del self.expenses[i]
                print("🗑️ Expense deleted successfully!")
                return
        print("⚠️ Expense ID not found!")

    def summary(self):
        if not self.expenses:
            print("⚠️ No expenses to summarize.")
            return

        total = sum(expense.amount for _, expense in self.expenses)
        print(f"\n💰 Total Expenses: ₹{total}")
        
        category_totals = {}
        for _, expense in self.expenses:
            category_totals[expense.category] = category_totals.get(expense.category, 0) + expense.amount
        
        print("---- Expenses by Category ----")
        for category, amount in category_totals.items():
            print(f"{category}: ₹{amount}")

# ------------------ CLI MENU ------------------
def main():
    tracker = ExpenseTracker()

    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Summary")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                amount = float(input("Enter amount: ₹"))
                category = input("Enter category (Food, Travel, Bills, etc.): ")
                description = input("Enter description (optional): ")
                expense = Expense(amount, category, description)
                tracker.add_expense(expense)
            except ValueError:
                print("⚠️ Invalid input! Please enter a valid number for amount.")

        elif choice == "2":
            tracker.view_expenses()

        elif choice == "3":
            try:
                expense_id = int(input("Enter Expense ID to delete: "))
                tracker.delete_expense(expense_id)
            except ValueError:
                print("⚠️ Invalid ID! Please enter a number.")

        elif choice == "4":
            tracker.summary()

        elif choice == "5":
            print("👋 Exiting Expense Tracker. Goodbye!")
            break

        else:
            print("⚠️ Invalid choice! Please select a valid option.")


if __name__ == "__main__":
    main()
