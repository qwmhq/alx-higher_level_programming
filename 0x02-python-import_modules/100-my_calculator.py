#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    argc = len(sys.argv)
    if argc != 4:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)
    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])
    if op not in "+-*/":
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    if op == '+':
        op_func = add
    elif op == '-':
        op_func = sub
    elif op == '*':
        op_func = mul
    else:
        op_func = div
    print("{} {} {} = {}".format(a, op, b, op_func(a, b)))
