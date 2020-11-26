    with open('src/convert.json','w') as currency:
        value = json.dumps(data, indent=2)
        currency.write(value)