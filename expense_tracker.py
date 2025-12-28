from expense import Expense
import datetime
import calendar


def main():
    print(f"running expense tracker!")
    expense_file_path = "expenses.csv"
    budget = 2000
    def red(text):
        return f"\033[91m{text}\033[0m"
    def green(text):
        return f"\033[92m{text}\033[0m"
    def yellow(text):
        return f"\033[93m{text}\033[0m"


    #Get user input for expense
    expense = get_user_expense(yellow)
   

    #write their expense to a file
    save_user_expense_to_file(expense,expense_file_path)

    #read file and summarize expense
    summarize_expenses(expense_file_path,budget,red,green,yellow)
   
   
def get_user_expense(yellow):
    print(f"getting user expense")
    expense_name = input("Enter expense name:")
    expense_amount = float(input("Enter expense amount:"))
    
    expense_categories =[
        "🍟food",
        "🏠rent",
        "🏬shopping",
        "🎬movie",
        "🎉fun",
        "🎶consert"
    ]
    while True:
        print("select a category: ")
        for i,category_name in enumerate(expense_categories):
            print(yellow(f" {i+1}.{category_name}"))
             
        value_range =f"[1-{len(expense_categories)}]"
        try:
            selected_index = int(input(f"Enter a category number{value_range}:"))
       

            if selected_index in range(len(expense_categories) + 1):
                selected_category = expense_categories[selected_index - 1]
                new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount)
                return new_expense
                
        except Exception:
             print("🎯enter a valid category range")          

        else:
            print("❌Invalid category.Please try again!") 
        
        
   
def save_user_expense_to_file(expense:Expense,expense_file_path):
    print(f"saving user expense:{expense} to {expense_file_path}")
    with open(expense_file_path,"a",encoding="utf-8") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")

    
def summarize_expenses(expense_file_path,budget,red,green,yellow):
    print(f"summarizing user expense")
    expenses: list[Expense] = []
    with open(expense_file_path,"r",encoding="utf-8") as f:
        lines=f.readlines()
        for line in lines:
            
            expense_name,expense_amount,expense_category= line.strip().split(",")
            
            line_expense = Expense(name=expense_name,category=expense_category,amount=(float(expense_amount)))
           
            expenses.append(line_expense)

    amount_by_category = {}
    for expense in expenses:
        key=expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount 
    print("✨Expenses by category:")
    for key,amount in amount_by_category.items():  
        print(f"  {key}:₹{amount}")  

    total_spent = sum([x.amount for x in expenses])   
    print(f"✨you've spent ₹{total_spent} this month!")      

    remaining_budget = budget-total_spent
    if remaining_budget<0:
        print(red("you are running out of budget please control it!!"))   
    else:
        print(green(f"Budget remaining:₹{remaining_budget}"))     

    today = datetime.date.today()

    total_days= calendar.monthrange(today.year,today.month)[1]
    remaining_days= total_days - today.day
    print(f"Remaining days in the current month is {remaining_days} days ")
    per_day_spend=remaining_budget/remaining_days
    print(red(f"Budget Per Day: ₹{per_day_spend}"))    

    
if __name__=="__main__":

    main()
    
