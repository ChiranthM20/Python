'''Ask the user for a sentence, count vowels, reverse the sentence, and replace spaces with -.
'''

sentence = input("Enter a sentence : ")

vowels="aeiouAEIOU"
vowel_count = sum(1 for x in sentence if x in vowels)

modified_sentence = sentence.replace(" ", "-")

print(sentence)
print(vowel_count)
print((sentence[::-1]))
