# 2. Write a Python program to split a sentence into individual words (tokens) and print the result.

def sentence_tokenizer():
    sentence = input("Enter a sentence: ")
    tokens = sentence.split()
    print("Tokens:", tokens)

sentence_tokenizer()