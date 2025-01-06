# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from customer_banking.cd_account import create_cd_account 
from customer_banking.savings_account import create_savings_account
# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    savings_balance = float(input('What is your savings account balance? '))
    savings_interest = float(input('What is the APR for the savings account? '))
    savings_month = float(input('How many months for the savings account? '))
    # Call the create_savings_account function and pass the variables from the user.
    interest_earned,updated_savings_balance = create_savings_account(savings_balance, savings_interest, savings_month)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print('Here are the details of the savings account.')
    print("Interest earned is: ", interest_earned)
    print("The balance is: $", updated_savings_balance)
    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_balance = float(input('What is your CD account balance? '))
    cd_interest = float(input('What is the interest rate for the CD account? '))
    cd_month = float(input('What is your months for the CD account? '))
    # Call the create_cd_account function and pass the variables from the user.
    cd_interest_earned,updated_cd_balance = create_cd_account(cd_balance, cd_interest,cd_month)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print('Here are the details of the CD account.')
    print("Interest earned is: ", cd_interest_earned)
    print("The balance is: $", updated_cd_balance)
if __name__ == "__main__":
    # Call the main function.
    main()
