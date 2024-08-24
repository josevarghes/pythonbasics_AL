def convert_temperature(temp,conversion = "C"):
    if conversion == "C" :
        return (temp*9/5)+32
    elif conversion == "F" :
        return (temp-32)*5/9
    
print(convert_temperature(10))
