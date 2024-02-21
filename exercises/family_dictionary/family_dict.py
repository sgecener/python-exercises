

my_family = {
    "sister": {
        "name": "Krista",
        "age": 42
    },
    "mother": {
        "name": "Cathie",
        "age": 70
    }
}

for k, v in my_family.items():

    name = v["name"]
    age = v["age"]
    print(f"{name} is my {k} and is {age} years old ")

