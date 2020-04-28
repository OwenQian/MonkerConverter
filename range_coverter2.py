import glob
import os
 
files = glob.glob("*.txt")

# Change this to your local directory the below stands for
# ~/Documents/poker/Monker/converted_ranges
base_path = os.path.join(os.path.expanduser("~"), "Documents", "poker", "Monker", "converted_ranges")
print("Putting converted files in:", base_path)

num_players = input("How many players are there in the sim? E.g. for HJ RFI it's 4-way.")
postions = ["LJ", "HJ", "CO", "BU", "SB", "BB"]
pos_map = {
    6: "LJ"
    5: "HJ"
    4: "CO"
    3: "BU"
    2: "SB"
    1: "BB"
}
first_pos = pos_map[num_players]

for file_name in files:
    next_path = base_path
    sizes = file_name.split(".")
    #change who's first in
    first_pos = "LJ"
    abc = postions.index(first_pos)
    open_raiser = postions[abc:]
    for size in sizes[:len(sizes)]:
        if size == "0":
            next_path = os.path.join(next_path, open_raiser[0]+"f")
            open_raiser.pop(0)
        elif size == "1":
            next_path = os.path.join(next_path, open_raiser[0]+"c")
            open_raiser.append(open_raiser[0])
            open_raiser.pop(0)
        elif size == "3":
            next_path = os.path.join(next_path, open_raiser[0]+"j")
            open_raiser.pop(0)
        elif size == "5":
            next_path = os.path.join(next_path, open_raiser[0]+"min")
            open_raiser.append(open_raiser[0])
            open_raiser.pop(0)
        else:
            next_path = os.path.join(next_path, open_raiser[0]+"r"+size[2:])
            open_raiser.append(open_raiser[0])
            open_raiser.pop(0)
    #if not os.path.exists(next_path):
    #    os.makedirs(next_path)
    lines = [line.rstrip('\n') for line in open(file_name)]
    string = ""
    while len(lines) > 0:
        hand = lines.pop(0) + ":"
        value = lines.pop(0).split(";", maxsplit=1)[0] + ","
        string += hand + value
    next_path += file_name
    print(next_path)
    break
    new_file = open(next_path, "w+")
    #print("string:", string)
    new_file.write(string)
    new_file.close()
