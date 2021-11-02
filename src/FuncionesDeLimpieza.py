import numpy as np;

def change(x):
    if x == 'Boat': #
        return 'Boating' #Esta función sirve para cambiar todos los valores de la columna type que sean boating mal escritos a boating
    elif x== 'Boatomg':
        return 'Boating'
    else:
        return x;

def change2(x):
    if x== '0': #Esta función sirve para cambiar todos los ceros a Nans, y así borrarlos luego más fácil
        return np.nan
    else:
        return x;

def change3(x):
    if x== ' N': #Esto sirve para corregir los datos dónde N está mal escrito y converit los casos dónde no se sabe sobre la fatalidad a Nan.
        return 'N'
    elif x== 'N ':
        return 'N'
    elif x== 'UNKNOWN':
        return np.nan
    else:
        return x;

def cambio1 (x):
    return 'White shark' #Estas tres sigueientes funciones, sirven para cambiar toda una columna a ese valor.

def cambio2 (x):
    return 'Bull shark'

def cambio3 (x):
    return 'Tiger shark';

def cambio4(x): #Aquí me he dado cuenta de que había un cero que en realidad mirando el date, era igual a 1959. Lo he intentado cambiar con el .loc pero no he sabido
    if x == 0.0:
        return 1959
    else:
        return x;