import argparse
import json
from typing import List

import solutions
from generator import cumulate, inverse_transform_sampling, generate_data


def load_distribution(distrib_file: str):
    distr = []
    with open(distrib_file, 'r') as f:
        for line in f:
            distr.append(line.split())
    distr = [[int(number), float(probability)] for number, probability in distr]
    return distr


def parse_params(file: str):
    with open(file, 'r') as f:
        params = json.load(f)

    dfile = params.get('distribution_file', None)
    if dfile:
        distribution = load_distribution(dfile)
        params['cumulated_distr'] = cumulate(distribution)
    else:
        params['cumulated_distr'] = None

    return params


def get_args():
    ap = argparse.ArgumentParser(description="Bin packing problem solver.\nGenerate data and run chosen algorithms.",
                                 epilog="Tal 2020")

    ap.add_argument('input',
                    metavar='input',
                    type=str,
                    help='Path co input file')
    args = ap.parse_args()

    return args


def generate(size: int, max_value: int, distribution: List):
    if distribution:
        return inverse_transform_sampling(size, distribution, already_cumulated=True)
    return generate_data(size, max_value)


def main():
    args = get_args()
    params = parse_params(args.input)

    print(params)

    algs_mapping = {
        'opt': solutions.optimal_solution,
        'nf': solutions.next_fit,
        'ff': solutions.first_fit,
        'lf': solutions.last_fit,
        'bf': solutions.best_fit,
        'wf': solutions.worst_fit
        # 'nfd','ffd', 'lfd', 'bfd', 'wfd'
    }

    for size in params['problem_sizes']:
        print("------")
        print(f"Problem size: {size}")
        for run in range(params['number_of_runs']):
            print(f"Run {run + 1}/{params['number_of_runs']}")
            generated = generate(size, params['bins_capacity'], params['cumulated_distr'])

            print(f"Generated data: {generated}")

            for alg in params['algorithms']:
                res = algs_mapping[alg](generated, params['bins_capacity'])
                print(f"Algorithm: {alg}")
                print(res)


if __name__ == '__main__':
    main()
