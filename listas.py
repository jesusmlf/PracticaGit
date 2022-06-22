def promedio(lista):
    contador = 0
    for i in lista:
        contador += i
    return contador

def run():
    lista = [1,2,3,4,5]
    print(promedio(lista))

if __name__ == '__main__':
    run()