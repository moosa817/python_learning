import json
from urllib.request import urlopen

def get_value():
    url = "https://api.exchangeratesapi.io/latest?base=USD"
    with urlopen(url) as response:
        source = response.read()
        data = json.loads(source)
        return 0
    
    with open('src/convert.json','w') as currency:
        value = json.dumps(data, indent=2)
        currency.write(value)
        return 0
    
    


