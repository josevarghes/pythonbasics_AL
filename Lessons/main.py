import calculations,greetings,menu

def main() :
    greetings.say_hello("User")
    menu.displya_menu()
    while True:
        choice = input("Please enter your option :")

        if choice == "1" :
            name = input("Please enter your name :")
            greetings.say_hello(name)

        elif choice == "2" :
            number1 = int(input("Enter your firt number :"))
            number2 = int(input("Enter your second number :"))
            operation = input("Please enter your operator (+,-,*,/) :")
            if operation == "+" :
                print("Result:",calculations.add(number1,number2))
            elif operation == "-" :
                print("Result:", calculations.subtract(number1,number2))
            elif operation == "*" :
                print("Result :", calculations.multiply(number1,number2))
            elif operation == "/" :
                try :
                    print("Result :", calculations.divide(number1,number2))
                except ValueError as e :
                    print(e)
            else :
              print("Inavalid operation, please choose an operation (+,-,*,/) ")

        elif choice == "3" :
            greetings.goodbye(name)
            break
        else :
          print("Invalid option, Please choose(1,2 or 3)")

if __name__ == "__main__" :
    main()






