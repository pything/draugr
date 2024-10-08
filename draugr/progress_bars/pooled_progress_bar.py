#!/usr/bin/env python3


from typing import (
    Any,
    Callable,
    Generator,
    Iterable,
    List,
    Mapping,
    MutableMapping,
    Optional,
    Sized,
)

from pathos.helpers import cpu_count
from pathos.multiprocessing import ProcessPool as Pool
from tqdm.auto import tqdm

__author__ = "Christian Heider Lindbjerg"
__all__ = [
    "parallel_map",
    "parallel_imap",
    "parallel_umap",
    "parallel_uimap",
    "sequential_map",
    "sequential_imap",
]
__doc__ = (
    r"""Map functions with tqdm progress bars for parallel and sequential processing."""
)


def _sequential(
    function: Callable,
    *iterables: Iterable,
    func_kws: Optional[Mapping] = None,
    **kwargs: MutableMapping
) -> Generator:
    """Returns a generator for a sequential map with a progress bar.

    Arguments:
        function(Callable): The function to apply to each element of the given Iterables.
        iterables(Tuple[Iterable]): One or more Iterables containing the data to be mapped.

    Returns:
        A generator which will apply the function to each element of the given Iterables
        sequentially in order with a progress bar."""

    # Determine length of tqdm (equal to length of shortest iterable)
    length = min(len(iterable) for iterable in iterables if isinstance(iterable, Sized))

    # Create sequential generator
    yield from tqdm(map(function, *iterables, **func_kws), total=length, **kwargs)


def _parallel(
    ordered: bool,
    function: Callable,
    *iterables: Iterable,
    func_kws: Optional[Mapping] = None,
    num_cpus: Optional[int] = None,
    **kwargs: MutableMapping
) -> Generator:
    """Returns a generator for a parallel map with a progress bar.

    Arguments:
        ordered(bool): True for an ordered map, false for an unordered map.
        function(Callable): The function to apply to each element of the given Iterables.
        iterables(Tuple[Iterable]): One or more Iterables containing the data to be mapped.

    Returns:
        A generator which will apply the function to each element of the given Iterables
        in parallel in order with a progress bar."""

    if func_kws is None:
        func_kws = {}

    if num_cpus is None:  # Determine num_cpus
        num_cpus = cpu_count()
    elif type(num_cpus) == float:
        num_cpus = int(round(num_cpus * cpu_count()))

    # Determine length of tqdm (equal to length of shortest iterable)
    length = min(len(iterable) for iterable in iterables if isinstance(iterable, Sized))

    map_type = "imap" if ordered else "uimap"
    pool = Pool(num_cpus)  # Create parallel generator
    map_func = getattr(pool, map_type)

    yield from tqdm(
        map_func(function, *iterables, (list(func_kws.values()),) * length),
        total=length,
        **kwargs
    )

    pool.clear()


def parallel_imap(
    function: Callable, *iterables: Iterable, **kwargs: MutableMapping
) -> Generator:
    """Returns a generator for a parallel ordered map with a progress bar."""
    return _parallel(True, function, *iterables, **kwargs)


def parallel_map(
    function: Callable, *iterables: Iterable, **kwargs: MutableMapping
) -> List[Any]:
    """Performs a parallel ordered map with a progress bar."""
    return list(parallel_imap(function, *iterables, **kwargs))


def parallel_uimap(
    function: Callable, *iterables: Iterable, **kwargs: MutableMapping
) -> Generator:
    """Returns a generator for a parallel unordered map with a progress bar."""
    return _parallel(False, function, *iterables, **kwargs)


def parallel_umap(
    function: Callable, *iterables: Iterable, **kwargs: MutableMapping
) -> List[Any]:
    """Performs a parallel unordered map with a progress bar."""
    return list(parallel_uimap(function, *iterables, **kwargs))


def sequential_imap(
    function: Callable, *iterables: Iterable, **kwargs: MutableMapping
) -> Generator:
    """Returns a generator for a sequential map with a progress bar."""
    return _sequential(function, *iterables, **kwargs)


def sequential_map(
    function: Callable, *iterables: Iterable, **kwargs: MutableMapping
) -> List[Any]:
    """Performs a sequential map with a progress bar."""
    return list(sequential_imap(function, *iterables, **kwargs))


if __name__ == "__main__":

    def asdasd() -> None:
        """
        :rtype: None
        """

        def add(a, b, *c):
            """description"""
            return a + b

        print(
            parallel_map(
                add, ["1", "2", "3"], ["a", "b", "c"], func_kws={"k": "sdafasd"}
            )
        )

    asdasd()
