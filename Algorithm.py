"""
Created at 6/12/16
__author__ = 'Sergio Padilla'
"""
from scipy import special
from math import pi, sin
from Planet import Planet
from planets_data import planets
DEFAULT_TOLERANCE = 1e-10


def get_planets_list():
    planetas = []
    for planet in planets:
        new_planet = planets[planet]
        planetas.append(Planet(epsilon=new_planet['epsilon'], period=new_planet['p'], semimajor_axis=new_planet['a']))

    return planetas


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
