import random

listOfWords = ["british", "suave", "integrity", "accent", "evil", "genius", "Downton"]

wordChosen = "accent"

print("🌟Hangman🌟")
print()

guessed = 0
lives = 6
usedLetters = []
wordList = ['_'] * len(wordChosen)

while True:
  letter = input("Choose a letter: ").lower()
  
  if letter not in usedLetters:
    usedLetters.append(letter)
  elif letter in usedLetters:
    print("You already guessed that letter!")
    print()
    print(f"You have {lives} lives left.")
    continue

  if letter in wordChosen.lower():
    guessed += 1
    print("Correct!")
    for i in range(len(wordChosen)):
      if wordChosen[i].lower() == letter:
        wordList[i] = letter
    for i in wordList:
      print(i, end='')
    print()
  
  else:
    print("Nope, not in there.")
    lives -= 1
    print(f"You have {lives} lives left.")
    print()
    
  if '_' not in wordList:
    print(f"Well done! You won with {lives} lives left")
    break
  elif lives == 0:
    print(f"You lost! The word was {wordChosen}")
    break
