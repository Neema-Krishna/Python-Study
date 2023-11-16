
import re
pin=input('enter a pin')
def add(pin):

    if len(pin) not in [6,7,8,9,10,11,12,13,14,15,16]:
        return 'invalid'

    if re.search('[a-z]',pin):
        if re.search('[A-Z]',pin):
            if re.search('[0-9]',pin):
                if re.search('[@#$%&*]',pin):
                    return 'ok'
    else:
        return 'not ok'
print(add(pin))
result=add(pin)
if result=='invalid':
    print('pin is not ok:please provide length in the range 1-16')
elif result=='not ok':
    print('pin iss not ok')
else:
    print('pin is ok')


pin=input('enter the pass')
import re






























