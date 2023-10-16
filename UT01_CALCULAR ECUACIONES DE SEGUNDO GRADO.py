#ecuaciones de segundo grado

from math import sqrt
a = float(input("Ingrese el valor de a: "))

if a == 0.0:
    b = float(input("Ingrese el valor de b: "))
    c = float(input("Ingrese el valor de c: "))
    if (b**2 - 4*a*c) >= 0.0:
        x1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
        x2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)
        print("la raíz real de la ecuacion es: ", x1)
        print("la raíz real de la ecuacion es: ", x2)
    else:
        print("No tiene raíz real")
else:
    print('error... la ecuación no es cuadrática')
