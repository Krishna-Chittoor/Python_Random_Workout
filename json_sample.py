import json

people_string = '''
{
    "people": [
        {
            "name": "Krishna Chittoor",
            "phone": "123-456-7890",
            "emails": ["test1@gmail.com", "test2@gmail.com"],
            "has_license": true
        },
        {
            "name": "Vennela Indrakanti",
            "phone": "012-345-6789",
            "emails": ["test3@gmail.com"],
            "has_license": true
        }
    ]
}
'''


# loads load json to string 
data=json.loads(people_string)

#print(type(data))

# for person in data['people']:
#     print(person['name'])

for person in data['people']:
    del person['phone']

# dumps load string to json 
new_string = json.dumps(data, indent = 2, sort_keys = True)
print(new_string)
