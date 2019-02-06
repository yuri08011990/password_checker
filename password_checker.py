data = input('Enter your password: ')

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


    #Phrases
    pass_cont  = 'The password contains'
    meet_req   = 'meets the requirements.'
    d_meet_req = 'does not meet the requirements.'
    secure     = 'Your password is secure.'
    n_secure   = 'Your password is not secure.'
    
        
    if is_long_enough == True and len(data) > 1:
        print ('{} {} characters which {}'.format(pass_cont, len(data), meet_req))
    elif len(data) == 1:
        print('{} {} character which {}'.format(pass_cont, len(data), d_meet_req))
    else:
        print ('{} {} characters which {}'.format(pass_cont, len(data), d_meet_req))
    
    if has_number == True and number > 1:
        print ('{} {} numbers which {}'.format(pass_cont, number, meet_req))
    elif has_number == True and number == 1:
        print ('{} {} number which {}'.format(pass_cont, number, meet_req))
    else:
        print ('{} {} numbers which {}'.format(pass_cont, number, d_meet_req))
    
    if has_uppercase == True and uppercase > 1:
        print ('{} {} uppercase characters which {}'.format(pass_cont, uppercase, meet_req))
    elif has_uppercase == True and uppercase == 1:
        print ('{} {} uppercase character which {}'.format(pass_cont, uppercase, meet_req))
    else:
        print ('{} {} uppercase characters which {}'.format(pass_cont, uppercase, d_meet_req))
    
    if has_lowercase == True and lowercase > 1:
        print ('{} {} lowercase characters which {}'.format(pass_cont, lowercase, meet_req))
    elif has_lowercase == True and lowercase == 1:
        print ('{} {} lowercase character which {}'.format(pass_cont, lowercase, meet_req))
    else:
        print ('{} {} lowercase characters which {}'.format(pass_cont, lowercase, d_meet_req))

    if is_long_enough and has_number and has_uppercase and has_lowercase == True:
        print (secure)
    else:
        print (n_secure)


checker(data)