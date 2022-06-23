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

def run():
    cantidad_alumnos = int(input("Ingrese la cantidad de alumnos: "))
    lista_alumnos= entrada_usuario(cantidad_alumnos)
    print(promedio(lista_alumnos))
def suma():
    return 5+9

if __name__ == '__main__':
    run()