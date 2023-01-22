words = []
while True:
    word = input("Enter a word (or press enter to stop): ")
    if word == '':
        break
    words.append(word)
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
for word, count in word_count.items():
    print(f'{word} occurs {count} times')
