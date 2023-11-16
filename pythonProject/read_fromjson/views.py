from json import load

with open("products.json") as f:
    data=load(f)
print(data)

# list1=[]
# for i in data:
#     if i['category']=='phonw':
#         list1.append(i['name'])
#
# print(list1)
#
# list2=[ i['name'] for i in data if i['category']=='phonw' ]
# print(list2)

# Highest price
# costly=max(data,key=lambda a:a['price'])
# print(costly)

# costly mobile
mobile=[ i for i in data if i['category']=='phonw' ]
#
# print(mobile)
v=max(mobile,key=lambda a: a['price'])
print(v['name'])

