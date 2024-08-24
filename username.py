correct_username = "admin"
correct_password = "12345"

attempts = 3



while attempts > 0 :
    username = input("Enter your username : ")
    password = input("Enter your password :")
    if username == correct_username and password == correct_password :
         print("You have successfully logged in. ")
         break
    else :
         print("You entered the wrong username or password ")
         attempts = attempts - 1 
         print(f"You have {attempts}left")
         if attempts < 1 :
                print("You have exceeded the limit, please try again later")