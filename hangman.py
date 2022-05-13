# Hangman
# Generování náhodného slova
import random
from hangman_2 import stages

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

#životy
lives = 6
print(stages[lives])

while "_" in hidden_word:
    #lives = 6
    guess = input("Zadejte hádané písmeno: \n").lower()
    for index in range(0, len(random_word)):
        if guess == random_word[index].lower():
            hidden_word[index] = guess
    #print(hidden_word)

            #ŠPATNĚ
            #print(f"Zbývá Ti {lives} život/životů.")
        #else:
            #lives -= 1
            #print(f"Zbývá ti {lives} život/životů.")
    #ŠPATNĚ
    #if guess == random_word[index].lower():
        #print(f"Zbývá Ti {lives} život/životů.")
    #else:
        #lives -= 1
        #print(f"Zbývá ti {lives} život/životů.")

    





# vypsání slova s podtržízky v normálmí podobě
    printed_word = ""
    for one_letter in hidden_word:
        printed_word += one_letter
    print(printed_word)
# kontrola životů
    if guess not in random_word:
        lives -= 1
        print(stages[lives])
        print(f"Zbývá Ti {lives} život/životy/životů.")
    else:
        print(f"Zbývá Ti {lives} život/životy/životů.")
# konec hry
    if lives == 0:
        print("Prohráli jste!!!")
        break

# kontrola vítěství
if "_" not in hidden_word:
    print("Vyhráli jste!!")






