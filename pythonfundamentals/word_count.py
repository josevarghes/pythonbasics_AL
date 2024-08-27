def word_count(senetence) :
    x = senetence.split()
    count = 0
    for i in x :
        count += 1
    return count
print(word_count("Today was a remarkable day for me."))