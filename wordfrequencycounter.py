#collecting input from the user
sentence = input("Please enter your sentence :").lower()

#splitting the given sentence into list
sentence = sentence.split()

words_frequency = {}

for word in sentence  :
    if word in words_frequency :
        words_frequency[word] = words_frequency[word] + 1
    else :
        words_frequency[word] = 1

for i,j in words_frequency.items() :
    print(i,j)






