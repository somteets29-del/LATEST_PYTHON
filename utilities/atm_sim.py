import random

print(" WELCOME TO THE FUTO BANK\n")
acc=int(input("Enter your account number:"))

balance = random.randint(1,999999999)
pint = 1200
tries = 0

while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transfer")
    print("5. Exit")
    print()
    
    choice = int(input("Choose an option: "))
    
#choice 1   
    if choice == 1:
        while tries < 3:
            pin= int(input("Enter your pin: "))
            if pin == pint:
                print("Your account balance is", balance)
            else:
                print("\nIncorrect pin")
                tries += 1
            if tries == 3:
                print("Account locked")   
                exit()     
 
#choice 2       
    elif choice == 2:
          depo = int(input("How much do you want to deposit: "))
          balance += depo
          print("You have successfully made a", depo, "naira deposit\n")
          print("Your new balance is", balance, "naira\n"
)

#choice 3
    elif choice == 3:     
            withd = int(input("Enter Withdrawal amount: "))
            pinw= int(input("Enter your pin: "))
            
            if withd > balance:
                print("Insufficient funds")
                
            if pinw == pint:
                balance -= withd
                print ("You have successfully withdrawed", withd, "naira\n")
                print ("Your new balance is", balance, "naira")
 
 #choice 4
    elif choice == 4:
          amt= int(input("Enter transfer amount (naira):"))
          trf_to = int(input("Enter Recipient Account:"))
         
          print()
          print("For transfer of ",amt,"naira to",trf_to)
          pind = int(input("Enter your pin: "))
          
          if pind == pint:
              balance -= amt
              print("You have successfully transfered",amt, "naira to",trf_to)
              print("Your new balance is", balance, "naira")
          else:
              print("Incorrect Pin")
              
#choice 5
    elif choice == 5:
        print("Thank you for banking with us")
        break
    else:
        print("Invalid selection\nTry again")