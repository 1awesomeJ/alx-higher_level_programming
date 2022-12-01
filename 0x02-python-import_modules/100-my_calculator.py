#!/usr/bin/python3

if __name__ == "__main__":
    import calculator_1 as calc
    import sys
    argv = sys.argv[1:]
    k = len(argv)
    operators = ['+', '-', '/', '*']
    if k != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    if argv[1] == '+':
        print("{:d} {:s} {:d} = {:d}".format(
            int(argv[0]), argv[1], int(argv[2]),
            calc.add(int(argv[0]), int(argv[2]))))
    elif argv[1] == '-':
        print("{:d} {:s} {:d} = {:d}".format(
            int(argv[0]), argv[1], int(argv[2]),
            calc.sub(int(argv[0]), int(argv[2]))))
    elif argv[1] == '*':
        print("{:d} {:s} {:d} = {:d}".format(
            int(argv[0]), argv[1], int(argv[2]),
            calc.mul(int(argv[0]), int(argv[2]))))
    elif argv[1] == '/':
        print("{:d} {:s} {:d} = {:d}".format(
            int(argv[0]), argv[1], int(argv[2]),
            calc.div(int(argv[0]), int(argv[2]))))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
