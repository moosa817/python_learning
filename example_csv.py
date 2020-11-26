name = input("Enter name: ")
age = input("Enter age: ")


with open('src/data.csv','a') as f:
    f.seek(0,0)
    content = ['\n',name+',',age]
    f.writelines(content)
