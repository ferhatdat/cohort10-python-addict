sentence = input("Enter string: ").lower()
text = ""
for i in sentence:
    if i.isalnum():
        text = text + i
if text == text[::-1]:
    print("Sentence is a palindrome")
else:
    print("Sentence is not a palindrome")