word = input()
letters = set(list(word))
letter_count = {letter: word.count(letter) for letter in letters}

if len(word) % 2 == 0:
    if all(count % 2 == 0 for count in letter_count.values()):
        print("yes")
    else:
        print("no")
else:
    odd_counts = sum(1 for count in letter_count.values() if count % 2 != 0)
    if odd_counts == 1:
        print("yes")
    else:
        print("no")

