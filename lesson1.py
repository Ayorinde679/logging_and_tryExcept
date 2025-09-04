def namecheck(name):
    if len(name) < 2:
        print("checking for debugging....")
        return "Invalid Name"
    elif name.isspace():
        print("checking if name is a space..")
        return "Invalid Name"
    elif name.isalpha():
        print("checking if name is an alphabet.")
        return "Name is Invalid"
    elif name.replace(' ','').isalpha():
        print("checking for full name.")
        return "Name is Invalid"
    else:
        print("failed all check...")
        return "Invalid Name"


print(namecheck("Alexander"))

"""for new dev you can use print to monitor your codes and detect errors, but as time goes and and production state comes 
you need to use logging module to monitor youtr code and functions"""
