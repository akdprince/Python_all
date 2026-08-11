import json

MyFiles = { 
    "people":[

        {
            "name": "Anik",
            "age": 29,
            "city": "Dhaka"

         },
         {
             "name": "Krishna",
             "age": 5100,
             "city": "Vrindavan"
         },
         {
                "name": "Rama",
                "age": 1000050,
                "city": "Ayodhya"
         },
         {
             "name": "Sita",
             "age": 1000000,
             "city": "Mithila"
         }
    ]

}

json_string = json.dumps(MyFiles, indent=4)

with open("/home/anik/lab/python/json/MyFiles.json", "w") as f:
    f.write(json_string)