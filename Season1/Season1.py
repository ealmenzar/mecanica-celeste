"""
Created at 1/12/16
__author__ = 'Sergio Padilla'
"""
from math import cos, sin, pi, sqrt

from Planet import Planet

DEFAULT_TOLERANCE = 1e-12


def newton_raphson(func, diff_func, u_0=pi, tolerance=DEFAULT_TOLERANCE):

    def get_next(u_n):
        return u_n-(func(u_n)/diff_func(u_n))

    previous = u_0
    current = get_next(previous)

    while abs(current-previous) < tolerance:
        previous = current
        current = get_next(previous)

    return current


def get_pos(planet, t):
    xi = 2*pi*t/planet.period

    def g(u):
        return u-planet.eccentricity*sin(u)

    def f(u):
        return g(u)-xi

    def diff_f(u):
        return 1-planet.eccentricity*cos(u)

    u = newton_raphson(f, diff_f)

    return [a*(cos(u)-planet.eccentricity), a*sqrt(1-planet.eccentricity*planet.eccentricity)*sin(u)]


if __name__ == '__main__':
    a = 1.000
    epsilon = 0.017
    period = 365.256
    tierra = Planet(epsilon, period, semimajor_axis=a)
    pos = get_pos(tierra, 29)

    print pos