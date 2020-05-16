import solutions
import solutions_count

time_algs_mapping = {
    'opt': solutions.optimal_solution,
    'nf': solutions.next_fit,
    'ff': solutions.first_fit,
    'lf': solutions.last_fit,
    'bf': solutions.best_fit,
    'wf': solutions.worst_fit,
    'nfd': solutions.next_fit_decreasing,
    'ffd': solutions.first_fit_decreasing,
    'lfd': solutions.last_fit_decreasing,
    'bfd': solutions.best_fit_decreasing,
    'wfd': solutions.worst_fit_decreasing
}

elementary_steps_algs_mapping = {
    'opt': solutions_count.optimal_solution,
    'nf': solutions_count.next_fit,
    'ff': solutions_count.first_fit,
    'lf': solutions_count.last_fit,
    'bf': solutions_count.best_fit,
    'wf': solutions_count.worst_fit,
    'nfd': solutions_count.next_fit_decreasing,
    'ffd': solutions_count.first_fit_decreasing,
    'lfd': solutions_count.last_fit_decreasing,
    'bfd': solutions_count.best_fit_decreasing,
    'wfd': solutions_count.worst_fit_decreasing
}
