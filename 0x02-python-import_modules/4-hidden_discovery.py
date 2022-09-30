#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    names = dir(hidden_4)
    underscore = "__"
    for i in range(len(names)):
        if underscore not in names[i]:
            print(names[i])
