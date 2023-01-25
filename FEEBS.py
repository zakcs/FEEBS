import time
import pyfiglet


print(" _____ _____ _____ ____ ____        _        ___  \n|  ___| ____| ____| __ ) ___|      / |      / _ \ \n| |_  |  _| |  _| |  _ \___ \      | |     | | | |\n|  _| | |___| |___| |_) |__) |     | |  _  | |_| |\n|_|   |_____|_____|____/____/      |_| (_)  \___/ ")
print(" ")
print(" ")
print("--------------------------------------------------")
print(" ")
while True:
 counter = 0
 

 def decrypt(encrypted_message):
     result = ""
     for letter in encrypted_message:
         if letter.isalpha():
             if letter.isupper():
                 shifted = chr((ord(letter) - ord('A') - counter + 26) % 26 + ord('A'))
                 result += shifted
             else:
                 shifted = chr((ord(letter) - ord('a') - counter + 26) % 26 + ord('a'))
                 result += shifted
         else:
             result += letter
     return result

 encrypted_message = input(f"Enter the encrypted message: ")

 #decrypting the message
 decrypted_message = decrypt(encrypted_message)

 import nltk
 nltk.download('words', quiet=True)
 from nltk.corpus import words
 from collections import Counter

 common_words = set(words.words())
 counter = 0
 best_iteration = 0
 best_count = 0
 best_word = ""
 best_message = ""

 print("Decrypting...")

 for i in range(0,26):
     counter += 1
     decrypted_message = decrypt(encrypted_message)
     matched_words = [word for word in decrypted_message.split() if word in common_words]
     if len(matched_words) > best_count:
         best_count = len(matched_words)
         best_iteration = counter
         best_message = decrypted_message
         word_counts = Counter(matched_words)
         best_word = word_counts.most_common(1)[0][0]

 print(f"\nIteration {best_iteration} had the most matched words with our word database: {best_count}")
 print(f"The decrypted message containing the common words is: {best_message}\n")
