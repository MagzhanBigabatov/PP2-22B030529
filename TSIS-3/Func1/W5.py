import itertools

def print_permutations(string):
    permutations = list(itertools.permutations(string))
    for permutation in permutations:
        print(''.join(permutation))

string = input("Enter a string: ")
print("All permutations:")
print_permutations(string)
