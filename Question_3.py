def fun(user):
    upper = 0
    lower = 0
    for i in range (len(user)):
        if user[i].isupper():
            upper = upper+1

        elif user[i].islower():
            lower = lower+1
            
    print(f"No. of Upper case characters: {upper}")
    print(f"No. of Lower case characters: {lower}")        
user = input("enter the words : ")
fun(user)