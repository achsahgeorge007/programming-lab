class Bank_Account :
    def Account(_account):
        _account._depositorName = name
        _account._number = accountNumber
        _account._type =  accountType
        _account._balance = accountBalance

name = input("Enter the name of account holder : ")
accountNumber = input("Enter the account number : ")
accountType = input("Enter the type of account : ")

initialAmount = int(input("Enter the initial value : "))
depositedAmount = int(input("Enter the amount to be depoisted : "))

checkBalance =(initialAmount + depositedAmount)
print("The amount in the account is : ", checkBalance)


print ("The name of accountholder : ", name)
print ("The account number of accountholder : ", accountNumber)
print ("The account type of accountholder : ", accountType)

withdrawAmount = int(input("Enter the amount to withdraw : "))
afterWithdrawal = (checkBalance - withdrawAmount)

print("The balance in the account is : ", afterWithdrawal)
