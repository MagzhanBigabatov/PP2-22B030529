def reverse(sent):
    words = sent.split()
    return " ".join(reversed(words))
sent = input()
print("Reversed sentence:", reverse(sent))