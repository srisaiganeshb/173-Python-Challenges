word = input("Enter the word to be verified: ")
if(word.lower()==word[::-1].lower()):
    print(word+" is a palindrome.")
else:
    print(word+" is not a palindrome.")