import json

MyFiles = { 
    "people":[

        {
            "name": "Anik",
            "age": 29,
            "city": "Dhaka",
            "country": True

         },
         {
             "name": "Krishna",
             "age": 5100,
             "city": "Vrindavan",
             "country": False
         },
         {
                "name": "Rama",
                "age": 1000050,
                "city": "Ayodhya",
                "country": False
         },
         {
             "name": "Sita",
             "age": 1000000,
             "city": "Mithila",
             "country": False
         }
    ]

}


json_string = json.dumps(MyFiles, indent=4)

# with open("/home/anik/lab/python/json/MyFiles.json", "w") as f:
#     f.write(json_string)

data = json.loads(json_string)

for person in data['people']:
    print(person['name'])