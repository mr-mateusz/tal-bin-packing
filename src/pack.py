import argparse
import os
from typing import List

available_args = ['opt', 'nf', 'ff', 'lf', 'bf', 'wfd', 'nfd', 'ffd', 'lfd', 'bfd', 'wfd']


def check_directory(output: str):
    if output is None:
        return
    split = os.path.split(output)
    if split[0] != '' and not os.path.isdir(split[0]):
        raise ValueError(f"Directory {split[0]} does not exists")


def check_elements(elements: List[int], capacity: int):
    if any([x > capacity for x in elements]):
        raise ValueError(f"Element value cannot be greater than bin capacity")


def get_args():
    ap = argparse.ArgumentParser(description="Bin packing problem solver",
                                 epilog="Tal 2020")

    ap.add_argument('--capacity',
                    metavar='capacity',
                    type=int,
                    help='Bin capacity')

    ap.add_argument('--algorithm',
                    type=str.lower,
                    choices=available_args,
                    help='Output file path',
                    nargs='+')

    ap.add_argument('--elements',
                    metavar='element',
                    type=int,
                    help='Bin capacity',
                    nargs='+')

    ap.add_argument('-o', '--output',
                    type=str,
                    help='Output file path')
    args = ap.parse_args()

    check_directory(args.output)

    check_elements(args.elements, args.capacity)

    return args


def main():
    try:
        args = get_args()
    except ValueError as e:
        print(f"Error in parsing args: {e}")


if __name__ == '__main__':
    main()
