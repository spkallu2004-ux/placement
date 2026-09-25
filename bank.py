class Bank:
    def __init__(self, customer_ID, account_number, min_balance, IFSC_code):
        self.customer_ID = customer_ID
        self.account_number = account_number
        self.min_balance = min_balance
        self.IFSC_code = IFSC_code

    def display(self):
        print("customer_ID:", self.customer_ID)
        print("account_number:", self.account_number)
        print("balance:", self.min_balance)
        print("IFSC_code:", self.IFSC_code)

my_account =Bank("C156", "12356", 1000, "IFSC001")
my_account.display()
