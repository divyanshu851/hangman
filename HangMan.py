import hangman_art as ha
import random

print(ha.logo)


word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

right_word = []

for _ in chosen_word:
    right_word.append("_")

life = 7
gaussed_right = True

while life > 0:
    print(right_word)
    gauss = input("Gauss a gauss :")
    for i in range(len(chosen_word)):
        if chosen_word[i] == gauss:
            right_word[i] = gauss
            gaussed_right = False
        
    if gaussed_right:

        life -= 1
        print(ha.HANGMANPICS[life])
        print(life)
    
    if "_" not in right_word:
        print("You Win")
        break

    gaussed_right = True

