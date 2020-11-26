import json

with open('src/data.json','r') as f:
    data = json.load(f)

for i in data['User']:
    print(i)    

with open('src/new_data.json','w') as f:
    json.dump(data,f,indent=2)