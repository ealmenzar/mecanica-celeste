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


def get_spin_matrix_x(angle):
    return np.array([[1, 0, 0], [0, cos(angle), -sin(angle)], [0, sin(angle), cos(angle)]])


def get_spin_matrix_z(angle):
    return np.array([[cos(angle), -sin(angle), 0], [sin(angle), cos(angle), 0], [0, 0, 1]])


def get_planets_data(t):
    planetas = get_planets_list()
    data = []
    for planet in planetas:
        data_planet = {'name': planet.name,
                       'position': planet.get_pos_newton_raphson(t),
                       'angular_moment_nr': planet.angular_moment_newton_raphson(t),
                       'u_nr': planet.get_u_newton_raphson(t),
                       'area_nr': planet.area_newton_raphson(0, t),
                       'energy': planet.energy(planet.get_u_newton_raphson(t)),
                       'energy_th': planet.th_energy()}
        data.append(data_planet)

    return data
