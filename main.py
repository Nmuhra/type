#let's measure your typing speed
print("let's measure how many letters you type per minute")
print("type the word 'quit' to stop")
words = 0
time = 0
while True:
    word = input("type a word: ")
    if word == "quit":
        break
    words += 1
    time += len(word)
    print("you typed", words, "words and", time, "letters")
print("you typed", words, "words and", time, "letters")
