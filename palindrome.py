def palindrome(word: str):
    return word[::-1] == word
while True:
    word = input ("Enter a palindrome :")
    print (f"{word} is palindrome !" if palindrome (word) else "not a palindrome!")
