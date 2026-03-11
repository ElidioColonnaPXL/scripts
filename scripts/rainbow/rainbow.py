# script for automatic lookup in dictionary of rainboe and a list in hashes.txt

rainbow_table_file = "md5woordenlijst.txt"
hash_file = "hashes.txt"

# Load rainbow table into dictionary
rainbow_table = {}

with open(rainbow_table_file, "r", encoding="latin-1") as f:
    for line in f:
        parts = line.strip().split()
        if len(parts) >= 2:
            hash_value = parts[0]
            password = " ".join(parts[1:]).strip('"')
            rainbow_table[hash_value] = password

# Read hashes to crack
with open(hash_file, "r") as f:
    hashes = [line.strip() for line in f]

print("Results:\n")

for h in hashes:
    if h in rainbow_table:
        print(f"{h}  ->  {rainbow_table[h]}")
    else:
        print(f"{h}  ->  NOT FOUND")