digit=input('Enter the digit')
list=[]
list1=['2','3','4','5','6','7','8','9']
list2=[]
dict={'1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}
dict1={'2':'Twenty','3':'thirty','4':'forty','5':'fifty','6':'sixty','7':'seventy','8':'eighty','9':'ninety'}
if int(digit) in range(1,10):
    print('Digit:',dict[digit].upper())
elif int(digit) in range(20,100):
    for i in str(digit):
        list2.append(i)
    one = list2[0]
    two = list2[1]
    if one in list1 and two==0:
        print('DIGIT',dict1[one])
    else:
        for i in str(digit):
            list.append(i)
        one=list[0]
        two=list[1]
        print('DIGIT:',dict1[one].upper(),dict[two].upper())
else:
    print('ERROR')






