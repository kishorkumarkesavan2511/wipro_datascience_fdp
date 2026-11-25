constraint_words = 200

input_text = input("Enter a sentence (max {constraint_words} words): ".format(constraint_words=constraint_words))    

search_word = input("Enter a word to search for: ")

words = input_text.split()

if search_word in words:
    print(f"The word '{search_word}' is present in the sentence.")
    print(f"The word '{search_word}' appears {words.count(search_word)} times in the sentence.")
else:
    print(f"The word '{search_word}' is not present in the sentence.")