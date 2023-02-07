print("Write how many heads and legs overall")
head = float(input())
legs = float(input())

RabbitNum = head*0.35
ChickenNum = head*0.66
if (int(RabbitNum))*4 + (int(ChickenNum))*2 == int(legs):
    print("Count of Rabbit: ", int(RabbitNum))
    print("Count of Chicken: ", int(ChickenNum))