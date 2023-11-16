a={}
email=[]
phone=[]
while True:
    print(' 1-ADD \n 2-UPDATE \n 3-DELETE \n 4-VIEW \n 5-EXIT')
    choice=int(input('Enter the Option:'))
    if choice == 1:
        b = {}
        Name = input('Enter Name:')
        Count_email = int(input('Enter Count of email:'))
        for i in range(0,Count_email):
            Email = input('Enter Email:')
            email.append(Email)
        Count_phone = int(input('Enter count of Phone-NO:'))
        for i in range (0,Count_phone):
            Phone = int(input('Phone.No:'))
            phone.append(Phone)
        b['NAME'] = Name
        b[ 'EMAIL']=email
        b['PHONE']=phone
        a[Name] = b
        print(a)

    elif choice==2:
        name=input('Enter the contact name')
        print(a[name])
        print('1.Name\n 2.Email \n 3.Phone-no')
        update=int(input('Enter detail to be updated'))

        if update==1:
            name1=input('Enter the name')
            a[name].update({'Name':name1})
            a[name1]=a[name]
            del a[name]
        elif update==2:
            dict=a[name]
            email=dict['EMAIL']
            print(email)
            selection=int(input('enter position of email to be updated'))
            new_email=input('enter new email')
            email[selection]=new_email
        else:
            dict=a[name]
            phone_no=dict['PHONE']
            print(phone_no)
            selection = int(input('enter position of phone-no to be updated'))
            new_number=input('Enter Phone number')
            phone_no[selection]=new_number

    elif choice==3:
        name=input('Enter the contact name')
        del a[name]
        print('Deleted')
    elif choice==4:
        name=input('Enter the contact name')
        print(a[name])
    else:
        break
