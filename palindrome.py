def check_palindrome(word: str):
    return word[::-1] == word

    
while True:
    word = input ("Enter a palindrome :")
    print (f"{word} is palindrome !" if check_palindrome (word) else "not a palindrome!")
    
