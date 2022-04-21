import random
import collections

def generateWord():
    words = []
    with open("words.txt") as file:
        listWords = file.readlines()
    for word in listWords:
        words.append(word.strip())
    randomWord = random.choice(words)
    return randomWord

word = generateWord()
countLettersWord = collections.Counter(word)
countLettersActualWord = dict(countLettersWord)

tries = 6
numberTries = 0
while tries > 0:
    underlines = "_____"
    n = input("Guess the word: ").lower()
    while len(n) != len(word):
      print("You are only supposed to type 5 letters a word!")
      n = input("Guess the word: ").lower()
    countLettersGuess = collections.Counter(n)
    countLettersActualGuess = dict(countLettersGuess)
    tries -= 1
    numberTries += 1
    for i in range(len(n)):
        if n[i].lower() == word[i]:
            underlines = underlines[0:i] + n[i].lower() + underlines[i:len(word) - 1]
        elif n[i].lower() in word and countLettersActualWord[n[i].lower()] >= countLettersActualGuess[n[i].lower()]:
            underlines = underlines[0:i] + "+" + underlines[i:len(word) - 1]
            countLettersActualGuess[n[i].lower()] -= 1
        else:
            underlines = underlines[0:i] + "-" + underlines[i:len(word) - 1]
            countLettersActualGuess[n[i].lower()] -= 1
    print(underlines)
    print("You are at " + str(tries) + " tries left!")
    if n.lower() == word and tries >= 0:
        print("Congratulations, you won the game! You won in " + str(numberTries) + " tries! :)")
        break
    elif tries == 0:
        print("Game over, you lost the game, The word was " + word + " :(")