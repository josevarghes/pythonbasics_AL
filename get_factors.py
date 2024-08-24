def get_factors(natural_number) :
    empty = []
    if natural_number < 0 :
        return empty
    else :
        for i in range(1,natural_number+1):
            if natural_number%i == 0 :
                empty.append(i)
        return empty
    
print(get_factors(20))


