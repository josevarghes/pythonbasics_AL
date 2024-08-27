def count_vowels(vowels) :
    x = ("aeiouAEIOU")
    count = 0
    for i in vowels :
        if i in x :
            count += 1

    return count

print(count_vowels("Alan"))

