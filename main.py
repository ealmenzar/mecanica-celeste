"""
Created at 1/12/16
__authors__ = 'Sergio Padilla / Marina Estévez / Irene Ocaña'
"""
from Utils import get_planets_list
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

if __name__ == '__main__':
    planets = get_planets_list()
    axis_x = []
    axis_y = []
    axis_z = []
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    print("Introduce el tiempo (en días terrestres): ")
    t = int(input())

    for planet in planets:
        position = planet.get_pos_newton_raphson(t)
        print(' *************************************************** ')
        print(planet.name)
        print(' *************************************************** ')
        print('La posición del planeta es: ', position)
        print('Momento angular con Newton-Raphson: ', planet.angular_moment_newton_raphson(50))
        print('Momento angular con Bessel: ', planet.angular_moment_bessel(50))
        print('Anomalía (u) con Newton-Raphson: ', planet.get_u_newton_raphson(50))
        print('Anomalía (u) con Bessel: ', planet.get_u_bessel(50))
        print('Distancia al Sol con Newton-Raphson: ', planet.distance_sun_newton_raphson(50))
        print('Distancia al Sol con Bessel: ', planet.distance_sun_bessel(50))
        print('Área Newton-Raphson (tiempo inicial: 0, tiempo final: t): ', planet.area_newton_raphson(0, t))
        print('Área Bessel (tiempo inicial: 0, tiempo final: t): ', planet.area_bessel(0, t))
        for i in range(0, int(planet.period+1)+10):
            position = planet.get_pos_newton_raphson(i)
            axis_x.append(position[0])
            axis_y.append(position[1])
            axis_z.append(position[2])

        ax.plot(axis_x, axis_y, axis_z)
        ax.scatter(position[0], position[1], position[2])
        ax.scatter(position[0], position[1], position[2], s=8 ** 2, c='k', alpha=0.5)
        ax.scatter(0, 0, s=10 ** 2, c='y', marker='*')
        ax.scatter(0, 0, s=11 ** 2, c='y', alpha=0.5)

        axis_x = []
        axis_y = []
        axis_z = []

    ax.set_xlim3d(-40, 40)
    ax.set_ylim3d(-40, 40)
    ax.set_zlim3d(-2, 2)

    plt.show()
