import glob
import os
 
f = glob.glob("*.rng")

base_path = os.path.join(os.path.expanduser("~"), "Documents", "poker", "Monker", "converted_ranges")
print("Putting converted files in:", base_path)
exit()
for x in range(len(f)):
    file_name = f[0]
    periods = file_name.count(".")
    # this format is for a MA
    next_path = base_path
    sizes = file_name.split(".")
    postions = ["LJ", "HJ", "CO", "BU", "SB", "BB"]
    #change who's first in
    first_pos = "LJ"
    abc = postions.index(first_pos)
    open_raiser = postions[abc:]
    for i in range(len(sizes)-1):
        if sizes[0] == "0":
            next_path = os.path.join(next_path, open_raiser[0]+"f")
            open_raiser.pop(0)
            sizes.pop(0)
        elif sizes[0] == "1":
            next_path = os.path.join(next_path, open_raiser[0]+"c")
            sizes.pop(0)
            open_raiser.append(open_raiser[0])
            open_raiser.pop(0)
        elif sizes[0] == "3":
            next_path = os.path.join(next_path, open_raiser[0]+"j")
            open_raiser.pop(0)
            sizes.pop(0)
        elif sizes[0] == "5":
            next_path = os.path.join(next_path, open_raiser[0]+"min")
            open_raiser.append(open_raiser[0])
            open_raiser.pop(0)
            sizes.pop(0)
        else:
            next_path = os.path.join(next_path, open_raiser[0]+"r"+sizes[0][2:])
            open_raiser.append(open_raiser[0])
            open_raiser.pop(0)
            sizes.pop(0)
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
    f.pop(0)
