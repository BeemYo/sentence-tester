letters = list("abcdefghijklmnopqrstuvwxyz ")
amount = []
sen = "the quick brown fox jumped over the lazy dog"
for i in letters:
    amount.append(0)

def print_2array(val, by):
    for i in range(len(amount)):
        print(by[i] + ": " + str(amount[i]))

def save(val, by, file):
    fil = open(file, "w+")
    fil.write(sen + "\n")
    for i in range(len(amount)):
        fil.write(by[i] + ": " + str(amount[i]) + "\n")
    fil.close()

for let in sen:
    index = letters.index(let)
    amount[index] += 1
save(amount, letters, "save.txt")
