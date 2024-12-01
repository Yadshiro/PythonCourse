#contacts
contacts = {
    "number" : 4,
    "students" : 
        [

            {'name' : 'Sarah Holderness' , 'email' :'sarah@exasmple.com'},
            {'name' : 'Harry Potter', 'email' :'harry@exasmple.com'},
            {'name' : 'Hermione Granger' , 'email' :'hermione@exasmple.com'},
            {'name' : 'Ron Weasley' , 'email' :'sarah@exasmple.com'}
            

        ]
        
}

print('Student emails')
for student in contacts ['students']:
    print(student['email'])