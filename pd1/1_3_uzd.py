hours = None
while hours == None: 
    try:
        hours = float(input('Enter Hours: '))
    except:
        print('Error, please enter numeric input')

rate = None
while rate == None: 
    try:
        rate = float(input('Enter Rate: '))
    except:
        print('Error, please enter numeric input')

pay = 0
if hours > 40:
    pay = 40 * rate + (hours-40) * rate * 2.1
else:
    pay = hours * rate

print('Pay: ' + str(pay))