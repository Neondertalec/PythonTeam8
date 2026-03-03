running = True

while(running):
    option = -1

    while option < 1:
        try:
            option = int(input("Enter the version of the code to use: \n 1 - 1.1 - basic \n 2 - 1.2 - overtime calculation \n 3 - 1.3 - input validation \n 4 - exit \n"))
        except:
            print("Enter a valid option")

        if option > 4: 
            option = -1
            print("Enter a valid option")
    
    match option:
        case 1:
            hours = float(input("Enter the hours:"))
            rate = float(input("Enter the rate:"))

            print("The resulting pay is : " + str(hours * rate))

        case 2:
            hours = float(input("Enter Hours: "))
            rate = float(input("Enter Rate: "))

            if hours > 40:
                regular_pay = 40 * rate
                overtime_hours = hours - 40
                overtime_pay = overtime_hours * rate * 2.10
                pay = regular_pay + overtime_pay
            else:
                pay = hours * rate

            print("Pay:", pay)
        
        case 3:

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
        
        case 4:
            running = False
