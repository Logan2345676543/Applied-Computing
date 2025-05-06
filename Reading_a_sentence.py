sentence = input("write a sentence. how many letter vowels's are there in it? ")
numberVowel = 0
for letter in sentence:
    if letter in ("a","e","i","o","u"):
        numberVowel +=1
print("The number of vowels's in the sentence is:", numberVowel)