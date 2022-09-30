#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv
    sum = 0
    length = len(args)
    if length > 1:
        for i in range(1, length):
            sum += int(args[i])
    print("{:d}".format(sum))
