from spellchecker import SpellChecker
corrector = SpellChecker()
for i in range(1,1000000):
    word = input("Enter a Word : ")
    if word in corrector:
        print("Correct")
    else:
        correct_word = corrector.correction(word)
        print("Correct Spelling is ", correct_word)