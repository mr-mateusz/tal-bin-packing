import argparse
import json
from typing import List, Dict, Tuple

import matplotlib.pyplot as plt

from generator import cumulate, inverse_transform_sampling, generate_data
from helpers import mappings
from helpers.decorators import run_and_capture_time

plt.style.use("ggplot")


def load_distribution(distrib_file: str) -> List:
    distr = []
    with open(distrib_file, 'r') as f:
        for line in f:
            distr.append(line.split())
    distr = [[int(number), float(probability)] for number, probability in distr]
    return distr


def parse_params(file: str) -> Dict:
    with open(file, 'r') as f:
        params = json.load(f)

    try:
        dfile = params['distribution_file']

        distribution = load_distribution(dfile)
        params['cumulated_distr'] = cumulate(distribution)
    except KeyError:
        params['cumulated_distr'] = None

    if 'problem_sizes' not in params:
        params['problem_sizes'] = range(params['problem_size_from'], params['problem_size_to'])

    if 'time' == params['type']:
        params['complexity_unit'] = 'time [ms]'
    else:
        params['complexity_unit'] = 'Elementary steps'

    params['algorithms'] = list(set(params['algorithms']))

    return params


def get_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description="Bin packing problem solver.\nGenerate data and run chosen algorithms.",
                                 epilog="Tal 2020")

    ap.add_argument('input',
                    metavar='input',
                    type=str,
                    help='Path to input file')

    ap.add_argument('-v',
                    '--verbose',
                    action='store_true',
                    help='Print info to stdout')

    args = ap.parse_args()

    return args


def generate(size: int, max_value: int, distribution: List) -> List[int]:
    if distribution:
        return inverse_transform_sampling(size, distribution, already_cumulated=True)
    return generate_data(size, max_value)


def prepare_and_save_plot(durations: List[Tuple], y_label: str):
    algs = list(set([d[0] for d in durations]))
    for alg in algs:
        alg_size = [a[1] for a in durations if a[0] == alg]
        alg_durs = [a[2] for a in durations if a[0] == alg]
        if len(alg_size) == 1:
            plt.scatter(alg_size, alg_durs, marker='.')
        else:
            plt.plot(alg_size, alg_durs)
    if 'opt' in algs:
        plt.yscale("log")
    plt.legend(algs)
    plt.xlabel("Problem size")
    plt.ylabel(y_label)
    plt.savefig("bin_packing_result.png")


def print_info(iter_index: int,
               max_iter: int,
               size: int,
               elements: List[int],
               durations: List[Tuple],
               results: List[List],
               complexity_unit: str):
    print(f'Iteration {iter_index + 1}/{max_iter}. Size: {size}')
    if size <= 20:
        print('Generated data: ')
        print(elements)
    for duration, result in zip(durations, results):
        print(f'Alg: {duration[0]}. Bins: {len(result)}. {complexity_unit}: {duration[2]}')
        if size <= 20:
            print(result)


def save_info_to_file(iter_index: int,
                      max_iter: int,
                      size: int,
                      elements: List[int],
                      durations: List[Tuple],
                      results: List[List],
                      complexity_unit: str):
    with open('output.txt', 'a') as f:
        f.write(f'Iteration {iter_index + 1}/{max_iter}. Size: {size}\n')
        if size <= 30:
            f.write('Generated data:\n')
            f.write(str(elements))
            f.write('\n')
        for duration, result in zip(durations, results):
            f.write(f'Alg: {duration[0]}. Bins: {len(result)}. {complexity_unit}: {duration[2]}\n')
            if size <= 30:
                f.write(str(result))
                f.write('\n')


def main():
    args = get_args()
    params = parse_params(args.input)

    if args.verbose:
        print('Bin packing solver')
        print(f'Bins capacity: {params["bins_capacity"]}')
        print(f'Algs : {params["algorithms"]}')

        write_info = print_info
    else:
        with open('output.txt', 'w') as f:
            f.write('Bin packing solver')
            f.write(f'Bins capacity: {params["bins_capacity"]}')
            f.write(f'Algs : {params["algorithms"]}')

        write_info = save_info_to_file

    durations = []
    for index, size in enumerate(params['problem_sizes']):
        generated = generate(size, params['bins_capacity'], params['cumulated_distr'])

        durations_for_size = []
        results_for_size = []
        for alg in params['algorithms']:
            if params['type'] == 'time':
                duration, res = run_and_capture_time(mappings.time_algs_mapping[alg],
                                                     generated,
                                                     params['bins_capacity'])
            else:
                duration, res = mappings.elementary_steps_algs_mapping[alg](generated, params['bins_capacity'])

            durations_for_size.append((alg, size, duration))
            results_for_size.append(res)

        write_info(index,
                   len(params["problem_sizes"]),
                   size,
                   generated,
                   durations_for_size,
                   results_for_size,
                   params["complexity_unit"])

        durations.extend(durations_for_size)

    prepare_and_save_plot(durations, params["complexity_unit"])


if __name__ == '__main__':
    main()
