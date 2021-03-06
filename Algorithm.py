"""
Created at 1/12/16
__authors__ = 'Sergio Padilla / Marina Estévez / Irene Ocaña'
"""
from scipy import special
from math import pi, sin
DEFAULT_TOLERANCE = 1e-12


def newton_raphson(func, diff_func, u_0=pi, tolerance=DEFAULT_TOLERANCE):

    def get_next(u_n):
        return u_n-(func(u_n)/diff_func(u_n))

    previous = u_0
    current = get_next(previous)

    while abs(current-previous) > tolerance:
        previous = current
        current = get_next(previous)

    return current


def bessel(xi, eccentricity, n):
    result = xi
    for i in range(1, n):
        result += 2/n*special.jv(i, eccentricity)*sin(xi)

    return result
