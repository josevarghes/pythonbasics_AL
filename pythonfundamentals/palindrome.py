def is_palindrome(word) :
    if word == word [::-1] :
        print(f"True, it's a palindrome word - {word}")

    else :
        print(f"False, it's not a palindrome word - {word}")

is_palindrome("malayalam")
