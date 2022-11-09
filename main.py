
def cantidadPalabras(l_palabras: list) -> list:
    # In: lista de palabras / Out: lista de cantidad de caracteres en cada
    # palabra
    # La funcion intentara contar la cantidad de caracteres en cada palabra de
    # la lista, y devolvera una lista con la misma cantidad de elementos donde
    # en cada posicion este la cantidad de caracteres de dicha palabra, en
    # caso de que uno de los elementos no sea un string devolvera una lista
    # vacia y una advertencia

    l_cantidad_letras = []
    for palabra in l_palabras:
        # Agrego a la lista de salida la longitud de cada palabra
        try:
            l_cantidad_letras.append(len(palabra))
        # Si el elemento de la lista no es str notifica y devuelve
        except TypeError:
            print("No es posible procesar la lista")
            print(f"El valor {palabra} no es un string")
            return []
    return l_cantidad_letras


if __name__ == "__main__":
    print("Test con todos elementos strings")
    print(cantidadPalabras(["perro", "elefante", "dragón","duende"]))
    print("Test con uno de los elementos int")
    print(cantidadPalabras(["perro", "elefante", "dragón",0,"duende"]))
