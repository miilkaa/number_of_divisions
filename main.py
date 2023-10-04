

def divisions(n:int, divisor:int):
    '''
    Calculate how many times a number can be divided by a given number.

    n: Number to divide

    divisor: Divisor
    '''
    quotient = None
    counter = 1
    if divisor == 0:
        print('Cannot division by zero')
    elif n < divisor:
        return 0 
    else:
        quotient = int(n / divisor)
        reminder = int(n % divisor)
        if reminder == 0:
            print(f'{counter}. {n} / {divisor} = {quotient}')
        else:
            print(f'{counter}. {n} / {divisor} = {quotient}, reminder = {reminder}')

        while quotient > 1 and quotient >= divisor:
            counter = counter + 1
            q = int(quotient / divisor)
            reminder = int(quotient % divisor)

            if quotient < divisor:
                break    
            if reminder == 0:
                print(f'{counter}. {quotient} / {divisor} = {q}')
            else:
                print(f'{counter}. {quotient} / {divisor} = {q}, reminder = {reminder}')
            quotient = q

        return counter
                    
                
divisions(39798827072691145897, 3)                