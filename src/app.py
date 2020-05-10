import argparse
import os


def main():
    ap = argparse.ArgumentParser(description="Bin packing problem solver",
                                 epilog="Tal 2020")

    ap.add_argument('mode',
                    metavar='mode',
                    type=str.lower,
                    choices=['f', 'c', 'g'],
                    help='Input data mode. Console/File/Generate: F/C/G')

    ap.add_argument('output',
                    metavar='output',
                    type=str,
                    help='path to output directory')

    ap.add_argument('--input',
                    type=str,
                    action='store',
                    help='input file')

    ap.add_argument('--capacity',
                    type=int,
                    action='store',
                    help='bins capacity')

    ap.add_argument('--elements',
                    type=int,
                    action='store',
                    help='elements',
                    nargs='+')

    ap.add_argument('--size',
                    type=int,
                    action='store',
                    help='problem size',
                    nargs='+')

    ap.add_argument('--runs',
                    type=int,
                    action='store',
                    help='number of runs for each problem size')

    ap.add_argument('--distribution',
                    type=str,
                    action='store',
                    help='path to file with distribution that will be used to generate data')

    args = ap.parse_args()

    if not os.path.isdir(args.output):
        print(f"Invalid output directory path: {args.output}")
        exit()

    print(vars(args))
    print(args.output)


if __name__ == '__main__':
    main()
