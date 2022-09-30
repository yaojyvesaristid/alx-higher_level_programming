#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    args = sys.argv
    length = len(args)
    signs = ['+', '-', '*', '/']
    if length != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if args[2] not in signs:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(args[1])
    b = int(args[3])
    op = args[2]

    def f_add():
        res = add(a, b)
        print("{:d} + {:d} = {:d}".format(a, b, res))
        return res

    def f_sub():
        res = sub(a, b)
        print("{:d} - {:d} = {:d}".format(a, b, res))
        return res

    def f_mul():
        res = mul(a, b)
        print("{:d} * {:d} = {:d}".format(a, b, res))
        return res

    def f_div():
        res = div(a, b)
        print("{:d} / {:d} = {:d}".format(a, b, res))
        return res
    ops = {
        "+": f_add,
        "-": f_sub,
        "*": f_mul,
        "/": f_div
    }
    ops.get(op)()
