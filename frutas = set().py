frutas = set()

def agregar_fruta(fruta):
    frutas.add(fruta.lower())
    print(f"¡{fruta.capitalize()} ha sido agregada con éxito!")

def mostrar_frutas():
    if frutas:
        print("\nFrutas registradas:")
        for fruta in frutas:
            print(f"- {fruta.capitalize()}")
    else:
        print("\nNo hay frutas registradas.")

def buscar_fruta(fruta):
    if fruta.lower() in frutas:
        print(f"Sí, {fruta.capitalize()} está en la lista.")
    else:
        print(f"No, {fruta.capitalize()} no se encuentra registrada.")

# Ejemplo de uso
agregar_fruta("manzana")
agregar_fruta("pera")
agregar_fruta("manzana")  # Esta no se duplicará

mostrar_frutas()
buscar_fruta("manzana")
