#! /usr/bin/python3
import sys
import math
import matplotlib.pyplot as pyplot
import numpy

N_0 = 12
OMEGA_0 = numpy.float128(2 * numpy.float128(math.pi) / N_0)

def unit_step(n):
    result = 0
    if (n >= 0):
        result = 1
    #if
    
    return numpy.float128(result)
#def unit

def x_time(n):
    result = 0

    A = numpy.float128(7.0)
    k_0 = numpy.float128(2.0)
    theta = numpy.float128(20.0)
    
    #result =  A * math.cos((2 * math.pi * k_0 / N_0 * n) + theta)

    #result = unit_step(n) - unit_step(n - N_0)

    if (0 <= n <= N_0):
        result = numpy.float128(0.5)**numpy.float128(n)

    return result
#x_time

def dft_at_k(k):
    x_laplace_k = numpy.float128(0.0)
    
    for n in range(0, N_0):
        x_laplace_k += x_time(n) * numpy.float128(math.e)**(-1j * k * OMEGA_0 * n)
    #for n
    
    return x_laplace_k
#dft_at_k

def idft_at_n(n):
    x_time_n = numpy.float128(0.0)

    for k in range(0, N_0 - 1):
        x_time_n += dft_at_k(k) * numpy.float128(math.e)**(+1j * k * OMEGA_0 * n)
    #for k
    x_time_n /= N_0

    return x_time_n
#idft
    
def main(argc, argv):
    pyplot.figure()
    pyplot.title("y = x[n]")
    pyplot.xlabel("n")
    pyplot.ylabel("y = x[n]")
    pyplot.grid()
    pyplot.xlim(-1, (N_0-1) + 1)
    for n in range(0, (N_0-1) + 1):
        result = x_time(n)
        print("(" + str(n) + ", " +  str(result) + ")")
        print()
        pyplot.plot([n, n], [0, result], "ro-")
    #for n
    pyplot.ion()
    pyplot.show()
    input("Done plotting x[n]. Press any key to continue...")
    
    #k v real
    pyplot.figure()
    pyplot.xlabel("K")
    pyplot.ylabel("Magnitude")
    pyplot.grid()
    pyplot.xlim((-1, N_0))    
    #pyplot.ylim((-limit, limit))
    
    #k v imag
    pyplot.figure()
    pyplot.xlabel("K")
    pyplot.ylabel("Phase")
    pyplot.grid()
    pyplot.xlim((-1, N_0))
    #pyplot.ylim((-limit, limit))

    '''
    #real v imag
    pyplot.figure()
    pyplot.xlabel("Real")
    pyplot.ylabel("Imaginary")
    pyplot.grid()
    #pyplot.xlim((-1, N_0-1))
    #pyplot.ylim((-limit, limit))
    '''

    for k in range(0, N_0):
        result = dft_at_k(k)
        print(result.real)
        print(result.imag)
        print()
        pyplot.figure(2)
        pyplot.plot([k, k], [0, abs(result)], "ro-")
        #pyplot.scatter(k, result.real)
        pyplot.figure(3)
        pyplot.plot([k, k], [0, numpy.angle(result)], "ro-")
        #pyplot.scatter(k, result.imag)
        '''
        pyplot.figure(4)
        #pyplot.plot([result.real, result.real], [0, result.imag], "ro-")
        pyplot.scatter(result.real, result.imag)
        '''
    #for k
    pyplot.ion()
    pyplot.show()

    print()

    input("Done calculating DFT. Press any key to continue...")
    #pyplot.close("all")   

    pyplot.figure()
    pyplot.xlim(-1, (N_0-1) + 1)
    for n in range(0, N_0):
        result = idft_at_n(n)
        print(abs(result))
        pyplot.plot([n, n], [0, abs(result)], "ro-")
    #for n
    pyplot.ion()
    pyplot.show()

    input("Done calculating IDFT. Press any key to continue...")
    pyplot.close("all")
    
    return 0
#main

sys.exit(main(len(sys.argv), sys.argv))
