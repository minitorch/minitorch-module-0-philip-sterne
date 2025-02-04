"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implement for Task 0.1.
def mul(x: float, y: float) -> float:
    return x * y


def id(x: float) -> float:
    return x


def add(x: float, y: float) -> float:
    return x + y


def neg(x: float) -> float:
    return -x


def lt(x: float, y: float) -> bool:
    return x < y


def eq(x: float, y: float) -> bool:
    return x == y


def max(x: float, y: float) -> float:
    return x if x > y else y


def is_close(x: float, y: float) -> bool:
    return abs(x - y) < 1e-2


def sigmoid(x: float) -> float:
    return 1.0 / (1.0 + math.exp(-x)) if x >= 0 else math.exp(x) / (1.0 + math.exp(x))


def relu(x: float) -> float:
    return max(0, x)


def log(x: float) -> float:
    return math.log(x)


def exp(x: float) -> float:
    return math.exp(x)


def log_back(x: float, y: float) -> float:
    return y / x


def inv(x: float) -> float:
    return 1 / x


def inv_back(x: float, y: float) -> float:
    return -1 / (x**2) * y


def relu_back(x: float, y: float) -> float:
    return y if x > 0 else 0


# ## Task 0.2


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


# TODO: Implement for Task 0.3.
def map(fn: Callable[[float], float], l: Iterable[float]) -> Iterable[float]:
    return [fn(x) for x in l]


def zipWith(
    fn: Callable[[float, float], float], l1: Iterable[float], l2: Iterable[float]
) -> Iterable[float]:
    return [fn(x, y) for x, y in zip(l1, l2)]


def reduce(
    fn: Callable[[float, float], float], l: Iterable[float], init: float
) -> float:
    return init if not l else reduce(fn, l[1:], fn(init, l[0]))


def negList(l: Iterable[float]) -> Iterable[float]:
    return map(neg, l)


def addLists(l1: Iterable[float], l2: Iterable[float]) -> Iterable[float]:
    return zipWith(add, l1, l2)


def sum(l: Iterable[float]) -> float:
    return reduce(add, l, 0)


def prod(l: Iterable[float]) -> float:
    return reduce(mul, l, 1)
