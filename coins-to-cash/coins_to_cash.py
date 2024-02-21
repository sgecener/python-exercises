
def calculate_dollars(pennies, dimes, quarters, nickels):
    return {
        "pennies" : pennies * 0.01, 
        "nickels" : nickels * .05,
        "dimes" : dimes * 0.1,
        "quarters" : quarters * 0.25
    }

dollar_amount = calculate_dollars(pennies=342, nickels=9, dimes=32, quarters=4)

total_dollars = sum(dollar_amount.values())

print(f'${total_dollars}')