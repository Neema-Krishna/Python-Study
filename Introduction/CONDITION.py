# age=int(input('enter your age'))
# health=input('enter your condition of health')
# card=input('bpl or apl')
# dose=input('First dose-1/Second dose-2')
#
# if age>=60:
#     if health=='critical':
#         if card=='bpl':
#             print('not eligible due to health')
#         else:
#             print('not eligible due to status and health')
#     elif health=='not ok':
#         if card=='bpl':
#             print('eligible after taking test')
#         else:
#             print('not elgigble due to status')
#     else:
#         if card=='bpl':
#             print('eligible')
#         else:
#             print('not eligble due to status')
#
# if age>=20:
#     if health=='critical':
#         if card=='lpl':
#             print('not eligible due to health')
#         else:
#             print('not eligible due to status and health')
#     elif health=='not ok':
#         if card=='bpl':
#             print('elible after taking test')
#         else:
#             print('not eligble due to status')
#     else:
#         if card=='bpl':
#             print('eligible')
#         else:
#             print('not eligble due to status')
# if age<20:
#     if health=='critical':
#         if card=='bpl':
#             print('not eligible due to health')
#         else:
#             print('not eligible due to status and health')
#     elif health=='not ok':
#         if card=='bpl':
#             print('eligible after taking test')
#         else:
#             print('not eligible due to status')
#     else:
#         if card=='bpl':
#             print('eligible')
#         else:
#print('not eligible due to status')
genre=int(input('GENRE:1-COMEDY:2-FICTION:3-GK'))
language=int(input('Malayalam-4:English-5'))
return1=int(input('MENTION IF YOY HAVE TO RETURN ANY OTHER BOOK:8-NO/9-YES'))

if genre==1:
    if language==4 or 5:
        if return1==8:
            types = int(input('6-To read from home/7-To read from library'))
            if types == 6:
                input('PLS MENTION YOUR ID NO')
                print('RETURN BOOK WITHIN 2 WEEKS')
            elif types == 7:
                print('PLS HANDOVER BOOK TO LIBRARIAN BEFORE 5:00 PM')
        else:
            print('PLEASE RETURN THE BOOK ')
elif genre==2:
    if language==4 or 5:
        if return1==8:
            types = int(input('6-To read from home/7-To read from library'))
            if types == 6:
                int(input('PLS MENTION YOUR ID NO'))
                print('RETURN BOOK WITHIN 2 WEEKS')
            elif types == 7:
                name=input('PLS INPUT BOOK NO/NAME')
                print('PLS HANDOVER BOOK:',name,'TO LIBRARIAN BEFORE 5:00 PM')
        else:
            print('PLEASE RETURN THE BOOK ')

elif genre==3:
    if language==5:
        if return1==8:
            if types == 6:
                types = int(input('6-To read from home/7-To read from library'))
                int(input('PLS MENTION YOUR ID NO'))
                print('RETURN BOOK WITHIN 2 WEEKS')
            elif types == 7:
                print('PLS HANDOVER BOOK TO LIBRARIAN BEFORE 5:00 PM')
        else:
            print('PLEASE RETURN THE BOOK ')
    else:
        print('ONLY AVAILABLE IN ENGLISH')














































