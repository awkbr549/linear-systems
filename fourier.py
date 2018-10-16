#! /usr/bin/python3
import math
import matplotlib.pyplot as pyplot
import numpy
from matplotlib.ticker import FormatStrFormatter

PERIOD = 2 * math.pi
N = 100
SMOOTHNESS = 1000.0
print(str(SMOOTHNESS))
RANGE = 2.0

def unit_step(t):
    result = 1.0
    if (t == 0):
        result = 0.5
    elif (t < 0):
        result = 0.0
    return result

def rect(t):
    result = unit_step(t) - unit_step(t-1)
    return result

def hw_5_q_5(t):
    #result = rect(t+2) + (2 *rect(t+1)) + (2 *rect(t)) + rect(t-1)
    result = unit_step(t+2) + unit_step(t+1) - unit_step(t-1) - unit_step(t-2)
    return result

def hw_5_q_5_fourier(t):
    A = 5.0
    result = 0.0
    for n in range(1, N+1):
        temp = math.sin(2.0 * math.pi * n / 3.0)
        temp += math.sin(math.pi * n / 3.0)
        temp *= (2.0 / math.pi / n)
        temp *= math.cos(math.pi * n * t / 3.0)
        result += temp
    result += 1
    return result

def square_wave(t):
    temp = math.sin(t)
    result = 0.0
    if (temp < 0):
        result = -1.0
    elif (temp > 0):
        result = 1.0
    return result

def square_wave_fourier(t):
    result = 0.0
    for n in range(1, N+1):
        temp = (2.0 - math.cos(-math.pi * n) - math.cos(math.pi * n))
        temp *= (1.0 / math.pi / n)
        temp *= math.sin(n * t)
        result += temp
    return result

def sawtooth_wave(t):
    result = t % PERIOD
    return result

def sawtooth_wave_fourier(t):
    result = 0.0
    for n in range(1, N+1):
        temp = math.sin(n * t)
        temp *= (-2.0 / n)
        result += temp
    result += math.pi
    return result

def saw_and_unit_wave(t):
    A = 3.0
    result = min(A * ((t + 1.0) % 2), A)
    return result

def saw_and_unit_wave_fourier(t):
    A = 3.0
    result = 0.0
    for n in range(1, N+1):
        temp_a = (A / (math.pi**2) / (n**2))
        temp_a *= (1 - math.cos(-math.pi * n))
        temp_a *= math.cos(math.pi * n * t)

        temp_b = (A / math.pi / n)
        temp_b *= (-math.cos(math.pi * n))
        temp_b *= math.sin(math.pi * n * t)

        result += (temp_a + temp_b)
    result += (3.0 * A / 4.0)
    return result










t = -RANGE * PERIOD
plot_array_x = []
plot_array_exact_y = []
plot_array_approx_y = []
while (t <= RANGE * PERIOD):
    plot_array_x.append(t)
    plot_array_exact_y.append(saw_and_unit_wave(t))
    plot_array_approx_y.append(saw_and_unit_wave_fourier(t))
    t += (PERIOD / SMOOTHNESS)



















#the fourier transform
pyplot.figure()
max_approx_y = 1.5 * max(abs(max(plot_array_approx_y)),
                         abs(min(plot_array_approx_y))
                         )
min_approx_y = -max_approx_y
#x-axis
pyplot.plot([-t, t], [0, 0], color="black")
#y-axis
pyplot.plot([0, 0], [min_approx_y, max_approx_y], color="black")
#the fourier transform data
pyplot.plot(plot_array_x, plot_array_approx_y, color="red")
#plotting this data
pyplot.xticks(numpy.arange(min(plot_array_x),
                           max(plot_array_x)+1,
                           math.pi)
)
pyplot.axis([-((RANGE * PERIOD / 2.0) + 0.5),
             (RANGE * PERIOD / 2.0) + 0.5,
             min_approx_y,
             max_approx_y])
pyplot.ion();
pyplot.grid();
pyplot.show();

#the exact function
pyplot.figure()
max_exact_y = 1.5 * max(abs(max(plot_array_exact_y)),
                        abs(min(plot_array_exact_y))
                        )
min_exact_y = -max_exact_y
#x-axis
pyplot.plot([-t, t], [0, 0], color="black")
#y-axis
pyplot.plot([0, 0], [min_exact_y, max_exact_y], color="black")
#the exact function data
pyplot.plot(plot_array_x, plot_array_exact_y, color="blue")
#plotting this data
pyplot.xticks(numpy.arange(min(plot_array_x),
                           max(plot_array_x)+1,
                           math.pi)
)
pyplot.xticks(numpy.arange(min(plot_array_x), max(plot_array_x)+1, math.pi))
pyplot.axis([-((RANGE * PERIOD / 2.0) + 0.5),
             (RANGE * PERIOD / 2.0) + 0.5,
             min_exact_y,
             max_exact_y])
pyplot.ion();
pyplot.grid();
pyplot.show();

input("Press `Enter' to exit.")
exit(0)
