"""
Created at 1/12/16
__author__ = 'Sergio Padilla'
"""
from Algorithm import get_planets_list


if __name__ == '__main__':
    planets = get_planets_list()
    for planet in planets:
        for i in range(0, 365):
            print(planet.get_pos_bessel(i))
