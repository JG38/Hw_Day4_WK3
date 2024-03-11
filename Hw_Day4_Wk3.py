class CashFlow:
    def __init__(self, income, expenses):
        self.income = income
        self.expenses = expenses
def rental_income(self):

        def rental_income(self):
            self.misc_income = int(input("\nWhat is your total monthly miscellaneous income? This can include income from sources like a side job, investments, etc...\n" \
                    "$ "))
            self.income += self.misc_income
            return self.income
    

def get_expenses(self):
        def get_expenses(self):
            self.property_taxes = int(input("\nWhat are your monthly property taxes?\n$ "))
            self.hoa_fees = int(input("\nWhat are your monthly HOA fees?\n$ "))
            self.lawn_care = int(input("\nWhat are your monthly lawn care expenses?\n$ "))
            self.vacancy_savings = int(input("\nWhat are your monthly vacancy savings?\n$ "))
            self.capital_expenditures = int(input("\nWhat are your monthly capital expenditures?\n$ "))
            self.property_management_cost = int(input("\nWhat are your monthly property management costs?\n$ "))
            self.mortgage = int(input("\nWhat is your monthly mortgage?\n$ "))
            self.expenses = self.property_taxes + self.hoa_fees + self.lawn_care + self.vacancy_savings + self.capital_expenditures + self.property_management_cost + self.mortgage
            return self.expenses
        def annual_income(self):
            return self.income * 12

        def annual_expenses(self):
            return self.expenses * 12

        def annual_cash_flow(self):
            return self.annual_income() - self.annual_expenses()
