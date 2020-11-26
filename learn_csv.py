import csv

with open('src/name.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    with open('src/new_names.csv','w') as new_file:
        fieldnames = ['First_name','Last_Name']
        csv_writer = csv.DictWriter(new_file,fieldnames=fieldnames,delimiter='\t')    

        csv_writer.writeheader()
        
        for line in csv_reader:
            del line['Email']
            csv_writer.writerow(line)



#with open('src/name.csv','r') as csv_file:
    #csv_reader = csv.DictReader(csv_file)

    #for line in csv_reader:
        #print(line['Email'])

#with open('src/name.csv','r') as csv_file:
#    csv_reader = csv.reader(csv_file)
#    with open('src/new_names.csv','w') as new_file:
#        csv_writer = csv.writer(new_file,delimiter='\t')
#
#        for line in csv_reader:
#            csv_writer.writerow(line)