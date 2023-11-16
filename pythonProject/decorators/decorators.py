# def sub(x,y):
#     if x<y:
#         (x,y)=(y,x)
#     return x-y
#
# def div(x,y):
#     if x<y:
#         (x,y)=(y,x)
#     return x/y
# print(sub(2,4))
# print(sub(2,4))

def swap_num(fn):

    def wrapper(x,y):
        if x<y:
            (x,y)=(y,x)
        return fn(x,y)

    return wrapper


@swap_num
def sub(x,y):
    if x<y:
        (x,y)=(y,x)
    return x-y
@swap_num
def div(x,y):
    if x<y:
        (x,y)=(y,x)
    return x/y
print(sub(2,4))
print(sub(2,4))




