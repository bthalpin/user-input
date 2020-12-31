def check_input_include(input_options, input_text = 'Please enter one of the following options', input_error = 'That is not a valid entry. ', display=True):
    '''
    This function asks the user for input and checks if the input entered is valid.
    You must enter a list of the valid input_options.  You can then change the text that is displayed 
    on the input by setting input_text = "Whatever text you want".  You can also change the error message 
    by setting input_error ='Whatever text you want'. By default the list of options will be displayed to 
    the user, but you can hide the list by setting display = False.
    '''
    wrong_input=True
    while wrong_input:
        if display:
            correct_input = input(f'{input_text}: {input_options}')
        else: 
            correct_input = input(f'{input_text}: ')

        try:
            if int(correct_input) in input_options:
                correct_input = int(correct_input)
        except:
            pass
        if correct_input in input_options:
            wrong_input = False
        else:
            print(input_error)
    return correct_input

def check_input_exclude(exclude_options, input_text = 'Please enter something', input_error = 'That is not a valid entry. ', display=True):
    wrong_input=True
    while wrong_input:
        if display:
            correct_input = input(f'{input_text} (must not include the following {exclude_options}): ')
        else:
            correct_input = input(f'{input_text}: ')

        if correct_input not in exclude_options and correct_input!='':
            wrong_input = False
        else:
            print(input_error)
        try:
            if int(correct_input) in exclude_options:
                wrong_input = True
                print(input_error)
        except:
            pass
    return correct_input