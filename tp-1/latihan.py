with open("./my_file", "r") as f:
    with open("./out", "a") as g:
        for line in f:
            print(line.lower().count("di "), file=g)
