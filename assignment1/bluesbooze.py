abbrev = {} 
with open("states.txt", "r") as f: 
    for line in f: 
        key, val = line.rstrip("\n").split(",")
        abbrev[key] = val 

def bluesbooze(str):
    final = abbrev[str]
    print final

