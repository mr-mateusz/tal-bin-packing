import argparse
import copy
from typing import List

import matplotlib.pyplot as plt
import numpy as np

from helpers import mappings
from helpers.decorators import run_and_capture_time


def get_args():
    ap = argparse.ArgumentParser(description="Bin packing problem solver",
                                 epilog="Tal 2020")

    ap.add_argument('-a',
                    '--algorithm',
                    type=str.lower,
                    help="Approximation algorithm",
                    required=True)

    ap.add_argument('elements',
                    metavar='element',
                    type=int,
                    help="Elements",
                    nargs='+')

    ap.add_argument('-c',
                    '--capacity',
                    metavar='capacity',
                    type=int,
                    default=10,
                    help='Bin capacity. Default to 10')

    ap.add_argument('-t',
                    '--time',
                    action='store_true',
                    help='Capture time instead of number of operations')

    args = ap.parse_args()

    return args


def visualise_and_save_bins(bins: List[List[int]], output_file: str, title: str):
    indexes = np.arange(len(bins))
    width = 0.35

    max_len = max(len(b) for b in bins)
    filled = copy.deepcopy(bins)
    for f in filled:
        f.extend([0] * (max_len - len(f)))
    layers = list(zip(*filled))

    bottom = [0] * len(bins)

    for layer in layers:
        plt.bar(indexes, layer, width, bottom=bottom)
        new_bottom = []
        for l1, l2 in zip(bottom, layer):
            new_bottom.append(l1 + l2)
        bottom = new_bottom

    plt.title(title)
    plt.savefig(output_file)
    plt.clf()


def main():
    args = get_args()

    if args.time:
        complexity_unit = 'time [ms]'
        duration_opt, res_opt = run_and_capture_time(mappings.time_algs_mapping['opt'],
                                                     args.elements,
                                                     args.capacity)

        duration_app, res_app = run_and_capture_time(mappings.time_algs_mapping[args.algorithm],
                                                     args.elements,
                                                     args.capacity)
    else:
        complexity_unit = 'Elementary steps'
        duration_opt, res_opt = mappings.elementary_steps_algs_mapping['opt'](args.elements, args.capacity)

        duration_app, res_app = mappings.elementary_steps_algs_mapping[args.algorithm](args.elements, args.capacity)

    print(f'Solve bin packing problem with optimal and chosen approximate algorithm.')
    print(f'Algorithms: opt, {args.algorithm}')
    print(f'Capacity: {args.capacity}')
    print(f'Elements: {args.elements}')
    print(f'Optimal solution. {complexity_unit.title()}: {duration_opt}. Bins: {len(res_opt)}')
    print(res_opt)
    print(f'Approximate solution. {complexity_unit.title()}: {duration_app}. Bins: {len(res_app)}')
    print(res_app)
    print(f'Approximate solution len/optimal solution len: {len(res_app)}/{len(res_opt)}={len(res_app) / len(res_opt)}')

    visualise_and_save_bins([[a] for a in args.elements], 'elements.png', 'Input elements')
    visualise_and_save_bins(res_opt, 'optimal_solution.png', 'Optimal solution')
    visualise_and_save_bins(res_app, 'approximate_solution', f'Approximate solution - {args.algorithm}')


if __name__ == '__main__':
    main()
