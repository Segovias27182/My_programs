#TAYLOR SERIES AND OTHER THINGS

#special numbers
e = 2.71828182846
pi = 3.1415926535898

#function to calculate the factorial of a number
def fac(n):
    if n == int(n):
        if n != 0:
            n_fac = n
            for i in range(1, n):
                n_fac = n_fac * i
        else:
            n_fac = 1
        return n_fac
    else:
        print('ERROR: fac function only accepts integer values')

#function to convert degrees to radians
def deg_to_rad(x):
    global pi
    rad = (x * 2 * pi) / 360
    return rad

#function to convert radians to degrees
def rad_to_deg(x):
    global pi
    deg = (x * 360) / (2 * pi)
    return deg

#function to calculate the sine of an angle
def sin(x): # x is an angle in radians
    sin_x = 0
    for n in range(0, 80):
        num = (-1) ** n
        num = num * (x) ** (2 * n + 1)
        den = 2 * n + 1
        den = fac(den)
        sin_x = sin_x + (num / den)
    return sin_x

#function to calculate the cosine of an angle
def cos(x): # x is an angle in radians
    sin_x = 0
    for n in range(0, 80):
        num = (-1) ** n
        num = num * (x) ** (2 * n)
        den = 2 * n
        den = fac(den)
        sin_x = sin_x + (num / den)
    return sin_x

#function to calculate the tangent of an angle
def tan(x): # x is an angle in radians
    tan_x = sin(x) / cos(x)
    return tan_x

#function to calculate the cotangent of an angle
def cot(x): # x is an angle in radians
    cot_x = 1 / tan(x)
    return cot_x

#function to calculate the secant of an angle
def sec(x): # x is an angle in radians
    sec_x = 1 / cos(x)
    return sec_x

#function to calculate the cosecant of an angle
def csc(x): # x is an angle in radians
    csc_x = 1 / sin(x)
    return csc_x