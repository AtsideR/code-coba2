def print_sequence(words):
    sentence = ""
    for word in words:
        sentence += word + " "
        print(sentence)

words = ["aku", "suka", "makan", "nasi"]
print_sequence(words)