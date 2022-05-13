# Hangman
# Generování náhodného slova
import random

words = ["harry", "roland", "albus", "hermiona", "tluosťoch"]
while True:
    new_name = input("Zadej jmeno: ")
    #words.append(new_name)
    if new_name == "":
        break
    words.append(new_name)
#print(words)  


random_word = words[random.randint(0,len(words) - 1)]
#print(random_word)

# Generování podtržítek
hidden_word = []
for one_letter in random_word:
    hidden_word.append("_")
#print(hidden_word)


while "_" in hidden_word:
    lives = 6
    guess = input("Zadejte hádané písmeno: \n").lower()
    for index in range(0, len(random_word)):
        if guess == random_word[index].lower():
            hidden_word[index] = guess
            #print(f"Zbývá Ti {lives} život/životů.")
        #else:
            #lives -= 1
            #print(f"Zbývá ti {lives} život/životů.")
    if guess == random_word[index].lower():
        print(f"Zbývá Ti {lives} život/životů.")
    else:
        lives -= 1
        print(f"Zbývá ti {lives} život/životů.")
    #print(hidden_word)


# vypsání slova s podtržízky v normálmí podobě
    printed_word = ""
    for one_letter in hidden_word:
        printed_word += one_letter
    print(printed_word)

# kontrola vítěství
if "_" not in hidden_word:
    print("Vyhráli jste!!")






