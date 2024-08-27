def add(num1,num2) :
    #adding the 2 numbers
    return num1 + num2 

def subtract(num1, num2) :
    #subtracting the 2 numbers
    return num1 - num2

def multiply(num1,num2) :
    #multiplying the 2 numbers
    return num1 * num2

def divide(num1, num2) :
     #dividing the 2 numbers
    if num2 == 0 :
        raise ValueError("can not be divisible by zero ")
    else :
         return num1/num2
    

