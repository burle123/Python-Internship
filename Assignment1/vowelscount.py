#  Accept a sentence and display the number of vowels in it.

sentence = input("Enter a sentence: ")
vowels = 'aeiouAEIOU'
count = 0
for i in sentence:
    if i in vowels:
        count += 1
print("Number of vowels in the sentence:", count)
