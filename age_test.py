age = int(input("how old are you ?:"))

def AgeForcast(a):
    if a > 100:
        print("Really old!")
    elif 100 >= a >= 50:
        print("older than me")
    elif 49 >= a >= 30:
        print("same as me")
    else:
        print("really young!")

AgeForcast(age)