stockDict = {
    "GM": "General Motors",
    "CAT":"Caterpillar",
    "EK":"Eastman Kodak",
    "GE": "General Electric"
}

purchases = [
    ( 'GE', 100, '10-sep-2001', 48 ),
    ( 'CAT', 100, '1-apr-1999', 24 ),
    ( 'GE', 200, '1-jul-1998', 56 ),
    ('GM' , 100, '2-jan-2002', 35)
]

totals = {}

for stock in stockDict:
    value = []
    for block in purchases:
        if block[0] == stock:
            value.append(block)
    totals[stock] = value

for k, v in totals.items():
    print(f"======{k}======")
    cost = 0
    for x in v:
        cost += x[1] * x [3]
        print(f"{x[1]} shares at {x[3]} dollars each on {x[2]}")
    print(f"Total value of stock portfolio: {cost}")
