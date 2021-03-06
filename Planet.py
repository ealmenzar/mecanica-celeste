"""
Created at 1/12/16
__authors__ = 'Sergio Padilla / Marina Estévez / Irene Ocaña'
"""
from math import sin, pi, cos, sqrt, radians
import Algorithm
import numpy as np
import Utils


class Planet:

    def __init__(self, name, epsilon, period, semimajor_axis, i, capital_omega, omega_bar):
        self.name = name
        self.eccentricity = epsilon
        self.period = period
        self.semimajor_axis = semimajor_axis
        self.semiminor_axis = semimajor_axis*sqrt(1-(pow(epsilon, 2)))
        self.mu = pow((2 * pi / period), 2) * pow(semimajor_axis, 3)
        self.h = -self.mu / (2 * semimajor_axis)
        self.i = radians(i)
        self.capital_omega = radians(capital_omega)
        self.omega = radians(omega_bar - capital_omega)
        
    def xi(self, t):
        return 2 * pi * t / self.period

    def position(self, u):
        pos = np.array([self.semimajor_axis * (cos(u) - self.eccentricity),
                        self.semimajor_axis * sqrt(1 - pow(self.eccentricity, 2)) * sin(u),
                        0])
        return np.dot(self.get_spin_matrix(), pos)

    def get_u_bessel(self, t):
        return Algorithm.bessel(self.xi(t), eccentricity=self.eccentricity, n=80)

    def get_pos_bessel(self, t):
        return self.position(self.get_u_bessel(t))

    def get_u_newton_raphson(self, t):
        def g(u):
            return u - self.eccentricity * sin(u)

        def f(u):
            return g(u) - self.xi(t)

        def diff_f(u):
            return 1 - self.eccentricity * cos(u)

        return Algorithm.newton_raphson(f, diff_f)

    def get_pos_newton_raphson(self, t):
        time = t % self.period
        return self.position(self.get_u_newton_raphson(time))

    def area(self, t1, t2, c):
        return self.module(c) * (t2-t1) / 2

    def distance_sun_newton_raphson(self, t):
        u = self.get_u_newton_raphson(t)
        return self.semimajor_axis * (1 - self.eccentricity * cos(u))

    def distance_sun_bessel(self, t):
        u = self.get_u_newton_raphson(t)
        return self.semimajor_axis * (1 - self.eccentricity * cos(u))

    def diff_eccentric_newton_raphson(self, t):
        u = self.get_u_newton_raphson(t)
        return 2 * pi / (self.period * (1 - self.eccentricity * cos(u)))

    def diff_eccentric_bessel(self, t):
        u = self.get_u_bessel(t)
        return 2 * pi / (self.period * (1 - self.eccentricity * cos(u)))

    def angular_moment_newton_raphson(self, t):
        u = self.get_u_newton_raphson(t)
        return [0, 0, pow(self.semimajor_axis, 2) * self.diff_eccentric_newton_raphson(t)
                * sqrt(1 - pow(self.eccentricity, 2)) * (1 - self.eccentricity * cos(u))]

    def angular_moment_bessel(self, t):
        u = self.get_u_bessel(t)
        return [0, 0, pow(self.semimajor_axis, 2) * self.diff_eccentric_newton_raphson(t)
                * sqrt(1 - pow(self.eccentricity, 2)) * (1 - self.eccentricity * cos(u))]

    def area_newton_raphson(self, t1, t2):
        return self.area(t1, t2, self.angular_moment_newton_raphson(t2))

    def area_bessel(self, t1, t2):
        return self.area(t1, t2, self.angular_moment_bessel(t2))

    def module(self, x):
        return sqrt(pow(x[0], 2) + pow(x[1], 2) + pow(x[2], 2))

    def energy(self, u):
        return((( (self.semimajor_axis**2) * (2*pi / (self.period * (1 - self.eccentricity * cos(u)))) ** 2 ) / 2) *
               (1 - (self.eccentricity**2) * cos(u) ** 2) -
               self.mu / (self.semimajor_axis * (1 - self.eccentricity * cos(u))))

    def th_energy(self):
        return - self.mu / (2* self.semimajor_axis)

    def get_spin_matrix(self):
        return np.dot(np.dot(Utils.get_spin_matrix_z(self.capital_omega), Utils.get_spin_matrix_x(self.i)), Utils.get_spin_matrix_z(self.omega))
