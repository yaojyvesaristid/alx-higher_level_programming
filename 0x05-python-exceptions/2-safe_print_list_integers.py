#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        count, no_int = 0, 0
        for i in range(x):
            print("{:d}".format(my_list[i]), end="")
            count += 1
        print()
        return count

    except (TypeError, ValueError):
        pass

    except IndexError:
        return count
