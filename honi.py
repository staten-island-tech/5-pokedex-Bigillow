def honi(sentence):
    frequent = 0
    stage = 1
    word = sentence.lower()

    for letter in word:
        if letter == "h" and stage == 1:
            stage += 1
        elif letter == "o" and stage == 2:
            stage += 1
        elif letter == "n" and stage == 3:
            stage += 1
        elif letter == "i" and stage == 4:
            stage += 1
        if stage == 5:
            stage = 1
            frequent += 1
    print(frequent)

honi("mjbvejahbvav")
