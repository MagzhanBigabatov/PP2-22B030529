def Pal(pali):
    word = pali[::-1]
    if word == pali:
        return True
    return False

pali = input()
print(Pal(pali))