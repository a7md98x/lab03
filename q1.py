dict = {}
def saveInfo():
    name = input("please enter your name:")
    salary = input("please enter your salary:")
    if name == "no" or salary == "no":
        return False
    else:
        dict[name]=salary
        return True



while saveInfo()!= False :
    print(dict)
