import json

# Sample data to write
data = [
            {
                "name": "John Doe",
                "age": 30,
                "city": "New York"
            },
            {
                "name": "Chrish",
                "age": 26,
                "city": "California"
            },
            {
                "name": "Eminem",
                "age": 25,
                "city": "Los Vegas"
            }
        ]

# for x in data:
#     if x["name"] == "Eminem" :
#         print(x)

data = bool([x for x in data if x["name"] == "Eminem"])
print(data)