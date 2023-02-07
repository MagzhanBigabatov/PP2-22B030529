def histo(num):
    
    for i in range(len(num)):
        list = []
        for j in range(num[i]):
            list.append("*")
        print("".join(list))

num = []
for i in range(3):
    num.append(int(input()))
histo(num)