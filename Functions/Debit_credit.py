print("Hello user!!")
print("Choice 1: Debit\nChoice 2: Credit\nChoice 3: Balance\n")

balance = 0

def debit():
    global balance
    debit_amount = int(input("Enter debited amount: "))
    balance -= debit_amount
    print("The debited amount is: ", debit_amount)
    print("New balance is: ", balance)

def credit():
    global balance
    credit_amount = int(input("Enter credited amount: "))
    balance += credit_amount
    print("The credited amount is: ", credit_amount)
    print("New balance is: ", balance)

def check_balance():
    global balance
    print("The present balance is: ", balance)

while True:
    choice = int(input("Enter your choice: \n"))
    if (choice == 1):
        debit()
    elif (choice == 2):
        credit()
    elif (choice == 3):
        check_balance()
    else:
        print("Bye user!!")
        break