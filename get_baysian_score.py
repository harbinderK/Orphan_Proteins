import sys

file_path = sys.argv[1]  # File containing all neighbor_list

with open(file_path, 'r') as file:
    data = file.readlines()

hash_dict = {}

for line in data:
    tokens = line.split()
    if len(tokens) >= 3:
        nei_value = float(tokens[2])
        hash_dict.setdefault(tokens[1], []).append(nei_value)

for identifier, values in hash_dict.items():
    score = 1
    for nei_value in values:
        s = (1000 - nei_value) / 1000
        score *= s
    sscore = 1 - score
    print(f"{identifier}\t{score}")


