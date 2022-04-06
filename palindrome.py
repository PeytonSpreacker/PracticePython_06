# ask user for a string input
string = input('Enter a word: ')
if len(string) < 3:
    print('Please try a longer word.')
    quit()
else :
# makes the input lowercase
    word = string.lower()
    print(word)
# determines whether the word is a palindrome
rev_string = reversed(word)
if list(rev_string) == list(word):
    print('This word is a palindrome.')
else:
    print('This word is not a palindrome.')