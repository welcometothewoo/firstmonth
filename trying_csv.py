import os
import csv

contacts = []



if not os.path.isfile("contacts.csv"):
    print('creating "contacts.csv"...')
   

        
def add():
    import csv
    global names, phone_numbers

    name = input("Please enter a name: ")
    phone_number = input("Please enter a name: ")

    if name != None and phone_number != None:
        contacts.append({'name': name, 'phone number': str(phone_number)})


    with open('contacts.csv', 'w', newline='') as f:

        #create csv writer
        fieldnames = ['name', 'phone number']
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()

        writer.writerows(contacts)
      
def delete():
    lines = list()
    memberName = input("Please enter a member's name to be deleted: ")
    with open('contacts.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            lines.append(row)
            for field in row:
                if field == memberName:
                    lines.remove(row)

    with open('contacts.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)
   
def update():
    lines = list()
    memberName = input("Please enter a member's name to edit: ")
    with open('contacts.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            lines.append(row)
            for field in row:
                if field == memberName:
                    newPhoneNumber = input("Please enter a new phone number: ")
                    lines.remove(row)
                    lines.append([memberName, newPhoneNumber])
    with open('contacts.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines) 
