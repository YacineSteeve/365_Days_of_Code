word, letters = set(input()), input()
wrongs = 0

for letter in letters:
    if letter in word:
        word.remove(letter)
    else:
        wrongs += 1

    if not word:
        print("WIN")
        break

    if wrongs == 10:
        print("LOSE")
        break
