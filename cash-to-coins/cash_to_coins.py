



"""
This is what should be returned from the function for that dollar amount

{
    "pennies": 4,
    "nickels": 1,
    "dimes": 1,
    "quarters": 34
}
"""

dollar_amount = 8.69

def calculate_coins(dollar_amount):
    # Converting dollar amount to cents
    cents = int(dollar_amount * 100)
    
    # Calculating the number of quarters
    quarters = cents // 25
    cents %= 25
    
    # Calculating the number of dimes
    dimes = cents // 10
    cents %= 10
    
    # Calculating the number of nickels
    nickels = cents // 5
    cents %= 5
    
    # The remaining cents are the number of pennies
    pennies = cents
    
    return {
        "pennies": pennies,
        "nickels": nickels,
        "dimes": dimes,
        "quarters": quarters
    }

dollar_amount = 8.69
coins = calculate_coins(dollar_amount)
print(coins)
