def revers_word(sentence) :
     x = sentence.split()
     reversed_list = []
     for i in x :
          reversed_list.append(i [::-1] )
     return " ".join(reversed_list)



     
    

print(revers_word(" He is a good guy."))

