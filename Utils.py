"""
Created at 10/1/17
__author__ = 'Sergio Padilla'

"""
from math import sin, cos
from Planet import Planet
from planets_data import planets
import numpy as np


def get_planets_list():
    planetas = []
    for planet in planets:
        new_planet = planets[planet]
        planetas.append(Planet(epsilon=new_planet['epsilon'], period=new_planet['p'], semimajor_axis=new_planet['a'],
                               i=new_planet['i'], omega=new_planet['omega']))

    return planetas


def get_spin_matrix_y(omega):
    return np.array([[cos(omega), 0, -sin(omega)], [sin(omega), 1, cos(omega)], [0, 0, 0]])


def get_spin_matrix_z(omega):
    return np.array([[cos(omega), -sin(omega), 0], [sin(omega), cos(omega), 0], [0, 0, 1]])

