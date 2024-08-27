
def print_digit_sum(b) :
    b = abs(b)
    
    a = 0
    for i in str(b) :
        a = a + int(i)
    return a
   
print(print_digit_sum(-123))

    

