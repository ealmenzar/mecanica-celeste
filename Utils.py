"""
Created at 1/12/16
__authors__ = 'Sergio Padilla / Marina Estévez / Irene Ocaña'
"""
from math import sin, cos
from Planet import Planet
from planets_data import planets
import numpy as np


def get_planets_list():
    planetas = []
    for planet in planets:
        new_planet = planets[planet]
        planetas.append(Planet(name=planet, epsilon=new_planet['epsilon'], period=new_planet['p'], semimajor_axis=new_planet['a'],
                               i=new_planet['i'], capital_omega=new_planet['capital_omega'], omega_bar=new_planet['omega_bar']))

    return planetas


def get_spin_matrix_y(angle):
    return np.array([[cos(angle), 0, -sin(angle)], [0, 1, 0], [sin(angle), 0, cos(angle)]])


def get_spin_matrix_z(angle):
    return np.array([[cos(angle), -sin(angle), 0], [sin(angle), cos(angle), 0], [0, 0, 1]])
