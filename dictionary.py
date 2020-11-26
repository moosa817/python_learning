user_input = input("Enter The Student Name: ")
name = ["Ali","Huzaifa"]
Student = {"Huzaifa":{"Name:":"Ali","Age:":14,"Class:":9},
"Ali":{"Name:":"Ali","Age:":15,"Class:":10}}

#c = Student['Ali']
#d = "Name:"
#print(c[d])

for i in name:
    if user_input == i:
        b = Student[user_input]
        for a in b:
            print(a,b[a])
    
        

     
        