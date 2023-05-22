'''
Complete the does_name_exist function. 
It should loop over all of the first/last name combinations in the first_names and last_names lists. 
If it finds a combination that matches the full_name it should return True. If the full name isn't found, it should return False instead.
'''

def does_name_exist(first_names, last_names, full_name):
    full_name_list = full_name.split()
    first_name_exists = False
    last_name_exists = False
    for i in first_names:
        if i == full_name_list[0]:
            first_name_exists = True

    for j in last_names:
        if j == full_name_list[1]:
            last_name_exists = True

    return first_name_exists and last_name_exists
