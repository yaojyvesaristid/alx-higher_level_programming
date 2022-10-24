#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count, no_int = 0, 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1

        except TypeError:
            no_int += 1

        except ValueError:
            no_int += 1

        except IndexError:
            raise

    print()
    return count
