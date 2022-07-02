from faulthandler import cancel_dump_traceback_later


def promedio(lista):
    contador = 0
    for i in lista:
        contador += i
    return contador/len(lista)

def entrada_usuario(cantidad_alumnos):
    arr = []
    for i in range(0,cantidad_alumnos):
        calificacion = 0
        calificacion = int(input("Ingrese la calificacion del alumno numero " + str(i+1) + ": "))
        arr.append(calificacion)
    return arr

def calificacion_alta(arr):
    max = arr[0]
    for i in arr:
        if i > max:
            max = i
    return max

def calificacion_baja(arr):
    min = arr[0]
    for i in arr:
        if i < min:
            min = i
    return min

def run():
    cantidad_alumnos = int(input("Ingrese la cantidad de alumnos: "))
    lista_alumnos= entrada_usuario(cantidad_alumnos)

    print(f"\nCalificacion mas alta: {calificacion_alta(lista_alumnos)}")
    print(f"Calificacion mas baja: {calificacion_baja(lista_alumnos)}")
    print(f"Promedio alumnos: {promedio(lista_alumnos)}")
    
if __name__ == '__main__':
    run()