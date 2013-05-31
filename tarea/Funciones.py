from lib.operaciones import *
from lib.operaciones impor HttpRequesResponseRedirect as RE

valor1 = int (raw_input ('ingrese un valor'))
valor2 = int (raw_input ('ingrese otro valor'))
operacion = rax_input ('¿Que operacione desea realizar: {s - r - m - d}')

if operacion.lower() == 's':
    print suma (valor1, valor2)
elif operacion.lower() == 'r':
    print resta (valor1, valor2)
elif operacion.lower() == 'm':
    print multiplicacion (valor1, valor2)
elif operacion.lower() == 'd':
    print division (valor1, valor2)    
