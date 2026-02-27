def space(y, t):
    list_y = 0
    list_x = 0
    both = 0
    for letter in y:
        list_y = letter
        for letter_2 in t:
            list_x = letter_2
            if list_y == list_x and list_y == "C" and list_x == "C":
                both += 1
            break
    print(both)


space("C....C", "CCC..C")
