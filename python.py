import csv

Nameslist = ['Name' , 'Email' , 'Number' , 'University' , 'Major']

with open('Data.csv','w') as new_file:
    csv_writer = csv.writer(new_file , dialect = 'excel' , delimiter = ',',lineterminator='\n')
    csv_writer.writerow(Nameslist)
Nameslist.clear()
i=0
user = 'start'
while (user != 'STOP'):
    var = 'Name'
    user = str(input('please enter your' + var + ':'))
    if user != 'STOP':
        Nameslist.append(user)
        var = 'Email'
        user = str(input('please enter your' + var + ':'))
        Nameslist.append(user)
        var = 'Number'
        user = str(input('please enter your' + var + ':'))
        Nameslist.append(user)
        var = 'Universities'
        user = str(input('please enter your' + var + ':'))
        Nameslist.append(user)
        var = 'Major'
        user = str(input('please enter your' + var + ':'))
        Nameslist.append(user)
        with open('Data.csv','a') as csv_file:
            csv_writer = csv.writer(csv_file , dialect = 'excel' , delimiter = ',',lineterminator='\n')
            csv_writer.writerow(Nameslist)
        k=0
        Nameslist.clear()