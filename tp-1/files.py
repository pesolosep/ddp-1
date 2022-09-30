f = open("./test", "w+")
lines = f.readlines()
for i, line in enumerate(lines):
    line = line.split()
    for i, word in enumerate(line):
        if "#" in word:
            word[i] = "h"
        if "@" in word:
            word[i] = "a"
    line = " ".join(line)
    lines[i] = line
print(lines)
f.writelines(lines)

f.close()
