def uniq(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique

lst = []
while len(lst)<=5:
    lst.append(int(input()))

print(uniq(lst))