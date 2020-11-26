Student = ["Suhaib", "basit", "Ahmed", "Ali"]


Student.append("Yasir")  # add value in the last
# Student.clear()            #clear the whole list
Student.remove("Ali")  # removes a value
# Student.reverse()           #reverse the list
# Student.sort(reverse=True)  #sort the values
Student.insert(0, "Huzaifa")  # insert New value

# Return the number of times the value appears inthe fruits list
print(Student.count("Suhaib"))

pop = Student.pop(1)

print(f"Popped {pop}")

print(Student)
