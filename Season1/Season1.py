"""
Created at 1/12/16
__author__ = 'Sergio Padilla'
"""
from Algorithm import get_planets_list
import matplotlib.pyplot as plt


if __name__ == '__main__':
    planets = get_planets_list()
    axis_x = []
    axis_y = []
    for planet in planets:
        print('Momento angular NR: ', planet.angular_moment_newton_raphson(50))
        print('Momento angular Bessel: ', planet.angular_moment_bessel(50))
        print('u NR: ', planet.get_u_newton_raphson(50))
        print('u Bessel: ', planet.get_u_bessel(50))
        for i in range(0, int(planet.period+1)):
            position = planet.get_pos_newton_raphson(i)
            axis_x.append(position[0])
            axis_y.append(position[1])

    plt.plot(axis_x, axis_y, 'r.')
    plt.axis([-40, 40, -40, 40])
    plt.show()
