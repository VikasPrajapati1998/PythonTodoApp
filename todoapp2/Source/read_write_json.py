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

# Writing JSON data to a file
with open('demo_data.json', 'a+') as file:
    json.dump(data, file, indent=4)
    
    
    
# Reading JSON data from a file
with open('demo_data.json', 'r+') as file:
    data = json.load(file)

print(data)