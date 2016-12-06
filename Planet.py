"""
Created at 1/12/16
__author__ = 'Sergio Padilla'
"""
from math import sin, pi, cos, sqrt
import Algorithm


class Planet:

    def __init__(self, epsilon, period, semimajor_axis):
        self.eccentricity = epsilon
        self.period = period
        self.semimajor_axis = semimajor_axis
        
    def xi(self, t):
        return 2 * pi * t / self.period

    def position(self, u):
        return [self.semimajor_axis * (cos(u) - self.eccentricity),
                self.semimajor_axis * sqrt(1 - self.eccentricity * self.eccentricity) * sin(u)]

    def get_pos_bessel(self, t):
        u = Algorithm.bessel(self.xi(t), eccentricity=self.eccentricity, n=80)

        return self.position(u)

    def get_pos_newton_raphson(self, t):
        def g(u):
            return u - self.eccentricity * sin(u)

        def f(u):
            return g(u) - self.xi(t)

        def diff_f(u):
            return 1 - self.eccentricity * cos(u)

        u = Algorithm.newton_raphson(f, diff_f)

        return self.position(u)
