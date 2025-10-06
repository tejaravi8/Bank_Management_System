customers = [ 
{"id": 1, "name": "Ravi", "balance": 5000, "pin": 1234, "loan_requests": []}, 
{"id": 2, "name": "Priya", "balance": 7000, "pin": 2345, "loan_requests": []}, 
{"id": 3, "name": "Suresh", "balance": 10000, "pin": 3456, "loan_requests": []} 
]

loan_requests = [ 
{"customer_id": 1, "amount": 5000, "status": "Pending"}, 
{"customer_id": 2, "amount": 10000, "status": "Pending"} 
]

#------------------------------- Customer menu -------------------------------

#Check Balance
def check_balance(id,pin):
    for customer in range(len(customers)):
        if customers[customer]['id']==id and customers[customer]['pin']==pin:
            cus_id=customer
            break
    else:
        print("\nIncorrect Id or Password\n")
        
    print(f"\n Your Current Balanace is {customers[cus_id]['balance']}\n")

#Deposite Money
def Deposite_money(id):
    for customer in range(len(customers)):
        if customers[customer]['id']==id:
            cus_id=customer
            Dep_money=int(input("\nEnter Your Deposite Money: "))
            break
    else:
        print("\nDetails Not Found\n")
    
    customers[cus_id]['balance']+=Dep_money
    print(f"\n{Dep_money} deposited successfully\n")

#Withdraw Money 
def withdraw_money(id,pin):
    for customer in customers:
        if customers[customer]['id']==id and customers[customer]['pin']==pin:
            cus_id=customer
            with_money=int(input("Enter Your Withdraw Money : "))
            break
    else:
        print("\nIncorrect Id or Password\n")
    
    if customers[cus_id]['balance']>=with_money:
        customers[cus_id]['balance']-=with_money
        print(f"\n{with_money} withdrawed Successfully\n")
    else:
        print("!!! Insufficient Balance !!!")

#Transfer Money
def Transfer_money():
    
    #sender
    print("\nsender:")
    id=int(input("Enter Your Id : "))

    for customer in range(len(customers)):
        if customers[customer]['id']==id:
            sender=customer
            transaction=True
            break
    else:
        print("\nDetails Not Found")
        transaction=False   
        
    #receiver
    if transaction:
        print("\nReceiver : ")
        receiver_id=int(input("Enter Receiver Id: "))
        for customer in range(len(customers)):
            if customers[customer]['id']==receiver_id:
                receiver=customer
                print(f"\nName: {customers[receiver]['name']}")
                transaction=True
                break
        else:
            print(f"\nDetails Not Found Regarding This id: {receiver_id}\n")
            transaction=False
        
    if transaction:
        sent_money=int(input("\nEnter Amount To Send : "))
        pin=int(input("Enter Your Pin : "))
        if customers[sender]['pin']==pin:
            if customers[sender]['balance']>=sent_money:
                customers[sender]['balance']-=sent_money
                customers[receiver]['balance']+=sent_money
                
                print("\nTransaction Successfull")
                print(f"\n{sent_money} withdrawed Successfully")
            else:
                print("\n!!! Insufficient Balance !!!")
        else:
            print("\n!!! Incorrect Password !!!")
    else:
        print("\nTransaction Failed Due to invalid Credentials")

#Apply Loan
def apply_loan(id,pin):
    
    for customer in range(len(customers)):
        if customers[customer]['id']==id and customers[customer]['pin']==pin:
            cus_id=customer
            loan=True
            break
    else:
        print("\nInvalid Id or Pin")
        loan=False
    
    if len(customers[cus_id]['loan_requests'])>1:
        if loan:
            loan_amt=int(input("Enter Loan Amount :"))
            customers[cus_id]['loan_requests'].insert(0,"applied_for_loan")
            loan_requests.append({"customer_id": customers[cus_id]['id'], "amount": loan_amt, "status": "Pending"})
            print("\nLoan Applid Successfull")
    else:
        print("\nYou Already applied for Loan")

#Loan Status
def loan_status(id,pin):
    for customer in range(len(customers)):
        if customers[customer]['id']==id and customers[customer]['pin']==pin:
            cus_id=customers[customer]['id']
            allow=True
            break
    else:
        print("\nInvalid Id or pin")
        allow=False
    
    if allow:
        for customer in range(len(loan_requests)):
            if loan_requests[customer]['customer_id']==cus_id:
                print(f"\n{loan_requests[customer]}")

#------------------------------- Admin menu -------------------------------

#View all accounts
def view_all_accounts():
    for customer in customers:
        print(customer)

#View Loan Requests
def view_loan_requests():
    for customer in range(len(loan_requests)):
        if loan_requests[customer]['status']=="Pending":
            print(loan_requests[customer])

#approve loan  or Reject Loan
def approve_loan():
    custom_id=int(input("Enter Customer id: "))
    for customer in range(len(customers)):
        if customers[customer]['id']==custom_id:
            cust_num=customer
    
    for customer in range(len(loan_requests)):
        if loan_requests[customer]['customer_id']==custom_id and loan_requests[customer]['status']=='Pending':
            loan_num=customer
    
    if ((loan_requests[loan_num]['amount']) < (customers[customer]['balance'])) and ( loan_requests[loan_num]['amount'] < 50000 ):
        loan_requests[loan_num]['status']="Success"
        customers[cust_num]['balance']+=loan_requests[loan_num]['amount']
        customers[cust_num]['loan_requests']=[]
        
    else:
        loan_requests[loan_num]['status']="Rejected"
        customers[cust_num]['loan_requests']=[]
        # print(" Rejected due to some requirements")

# Choose Option

while True:
    menu=input("Choose Option ( Admin / Customer ) (!! press exit to stop !!): ").strip().lower()
    if menu=='customer':
        while True:   
            print("\n====== Customer Menu ======\n")
            print("1.Check_balance")
            print("2.Deposite Money")
            print("3.Withdraw Money")
            print("4.Transfer Money")
            print("5.Apply for loan")
            print("6.View loan status")
            print("7.exit")

            option=int(input("\nenter your choice : "))

            if option==1:
                id=int(input("Enter Your Id : "))
                pin=int(input("Enter your Pin : "))
                check_balance(id,pin)
            elif option==2:
                id=int(input("Enter Your Id : "))
                Deposite_money(id)
            elif option==3:
                id=int(input("Enter Your Id : "))
                pin=int(input("Enter your Pin : "))
                withdraw_money(id,pin)
            elif option==4:
                Transfer_money()
            elif option==5:
                id=int(input("Enter Your Id : "))
                pin=int(input("Enter your Pin : "))
                apply_loan(id,pin)
            elif option==6:
                id=int(input("Enter Your Id : "))
                pin=int(input("Enter your Pin : "))
                loan_status(id,pin)
            elif option==7:
                print("Thanks for Using Bank Management System")
                break

    if menu=='admin':
        while True:
            print("\n===== Admin Menu =====\n")
            print("1. View All Accounts ")
            print("2. View Loan Requests ")
            print("3. Approve Loan or Reject Loan")
            # print("4. Reject Loan ")
            print("4. Exit ")
            
            option=int(input("Enter your option: "))
            
            if option==1:
                view_all_accounts()
                    
            if option==2:
                view_loan_requests()
            
            if option==3:
                approve_loan()
            
            if option==4:
                break

    if menu=="exit":
        break