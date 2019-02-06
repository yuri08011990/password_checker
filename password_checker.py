data = input('Enter password: ')

def checker(data):
    
    is_long_enough = False
    number = 0
    uppercase = 0
    lowercase = 0
    
    has_number = False
    has_uppercase = False
    has_lowercase = False
    
    if len(data) >= 10:
        is_long_enough = True
    
    for check in data:        
        if check.isdigit():
            number += 1
            if number >= 1:
                has_number = True
        elif check.isupper():
            uppercase += 1
            if uppercase >= 1:
                has_uppercase = True
        elif check.islower():
            lowercase += 1
            if lowercase >= 1:
                has_lowercase = True
    
        
    if is_long_enough == True:
        print ('The password contains', len(data), 'characters which meets the requirements.')
    else:
        print ('The password contains', len(data), 'characters which does not meet the requirements.')
    
    if has_number == True and number > 1:
        print ('The password contains', number, 'numbers which meets the requirements.')
    elif has_number == True and number == 1:
        print ('The password contains', number, 'number which meets the requirements.')
    else:
        print ('The password contains', number, 'numbers which does not meet the requirements.')
    
    if has_uppercase == True and uppercase > 1:
        print ('The password contains', uppercase, 'uppercase letters which meets the requirements.')
    elif has_uppercase == True and uppercase == 1:
        print ('The password contains', uppercase, 'uppercase letter which meets the requirements.')
    else:
        print ('The password contains', uppercase, 'uppercase letters which does not meet the requirements.')
    
    if has_lowercase == True and lowercase > 1:
        print ('The password contains', lowercase, 'lowercase letters which meets the requirements.')
    elif has_lowercase == True and lowercase == 1:
        print ('The password contains', lowercase, 'lowercase letter which meets the requirements.')
    else:
        print ('The password contains', lowercase, 'lowercase letters which does not meet the requirements.')

    if is_long_enough and has_number and has_uppercase and has_lowercase == True:
        print ('Your password is secure.')
    else:
        print ('Your password is not secure.')


checker(data)