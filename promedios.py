 # -*- coding: utf-8 -*-

from random import *
from math import *

"""
    Programa para calcular promedio y redondearlos a a una califacion entera
"""

matematicas = float(round(random() * randint(1,10), 2))
espanol = float(round(random() * randint(1,10), 2))
dibujo = float(round(random() * randint(1,10), 2))
computacion = float(round(random() * randint(1,10), 2))

print "matematicas: %.2f \n" % matematicas
print "espanol: %.2f \n" % espanol
print "dibujo: %.2f \n" % dibujo
print "computacion: %.2f \n" % computacion

promedio = (matematicas + espanol + dibujo + computacion) / 4

print "el promedio es: %.2f \n" % promedio

if (promedio - int(promedio)) >= .5:
    print "1.Redondeado seria: %d." % ceil(promedio)
else:
    print "2.Redondeado seria: %d." % floor(promedio)


