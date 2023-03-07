with open(r"1text.txt", 'r') as fp:
    lines = len(fp.readlines())
    print('Total Number of lines:', lines)