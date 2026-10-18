word = input("Enter the word to be verified: ")
l_index = 0
r_index = len(word)-1
is_palindrome = True

while(l_index < r_index):
    if(word[l_index].lower() != word[r_index].lower()):
        is_palindrome = False
        break
    l_index +=1
    r_index -=1

if(is_palindrome):
    print(word+" is a palindrome.")
else:
    print(word+" is not a palaindrome.")