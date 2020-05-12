from time import time
from typing import Tuple, Any, Callable


def run_and_capture_time(function: Callable, *args, **kwargs) -> Tuple[float, Any]:
    """Run passed function and capture execution time.

    Args:
        function: function to call
        *args: will be passed to function
        **kwargs: will be passed to function

    Returns:
        (duration [s], function result)
    """
    start_time = time()

    res = function(*args, **kwargs)

    duration = time() - start_time

    return duration, res
