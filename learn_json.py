import json

School = '''
{
    "Students":[
        {
            "Name":"Moosa",
            "Class":"XB",
            "Active":false
        },
        {
            "Name":"Hamza",
            "Class":"IXB",
            "Active":true
        }
    ]
}
'''

data  = json.loads(School)


for i in data['Students']:
    print("\n")
    for b in i:
        print(b,":",i[b])