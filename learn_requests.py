import requests

payload = {'username':'moosa','password':'moosa817'}
r = requests.get('http://httpbin.org/basic-auth/moosa/moosa817',auth=('moosa','moosa817'))

print(r.text)






#with open('src/computer.png','wb') as f:
    #f.write(r.content)