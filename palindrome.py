# it's a number or word that reads same forward and backard (madam)(12321)

text = input("Enter a word or number: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")