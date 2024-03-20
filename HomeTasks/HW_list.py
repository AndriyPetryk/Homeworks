phone_book = {
    'Tom' : 380987788,
    'Cris' : 380299333
}
while True:
    name_number = input('Write youre command, name and number phone if you want to create new contact: ')
    split_input = name_number.split()
    command = split_input[0]
    name = split_input[1]

    if command == 'stats':
        print(f'{len(phone_book)}')

    elif command == 'add':
        phone = split_input[2]
        phone_book.update({name: phone})

    elif command == 'delete':
       del phone_book[name]

    elif command == 'list':
        for people_name in phone_book.keys():
            print(people_name)


    elif command == 'show':
        print(f'{name} {phone_book.get(name)}')


    else:
        print(f"It's no command, please use: 'stats, add, list, delete or show'. ")
