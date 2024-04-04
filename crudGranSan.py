import pymongo

def main():
    pass

def menu():
    opcion = int(input(("1. Crear un registro \n2. Buscar un registro \n3. Actualizar un registro\n" +
                       "4. Eliminar un registro \n5. Salir\nDigite opción... ")))
    return opcion

def crear():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["gran_san"]
    collection = db["publicaciones"]
    id_publicacion = input("Ingrese el ID de la publicación: ")
    imagen = input("Ingrese la URL de la imagen de la publicación: ")
    video = input("Ingrese la URL del video de la publicación (deje en blanco si no hay): ")
    enlace = input("Ingrese el enlace de la publicación: ")
    texto = input("Ingrese el texto de la publicación: ")
    anuncio = input("¿Es un anuncio? (Sí/No): ").lower() == 'sí'
    personas_relacionadas = input("Ingrese las personas relacionadas a la publicación (separadas por comas): ").split(',')
    
    documento = {
        "id_publicacion": id_publicacion,
        "imagen": imagen,
        "video": video,
        "enlace": enlace,
        "texto": texto,
        "anuncio": anuncio,
        "personas_relacionadas": personas_relacionadas
    }
    insert_result = collection.insert_one(documento)
    print("ID del nuevo documento:", insert_result.inserted_id)

def consultar():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["gran_san"]
    collection = db["publicaciones"]
    id_publicacion = input("Ingrese el ID de la publicación a buscar: ")
    data = collection.find_one({"id_publicacion": id_publicacion})
    if data:
        print("Información de la publicación:")
        print("ID de publicación:", data["id_publicacion"])
        print("Imagen:", data["imagen"])
        print("Video:", data["video"])
        print("Enlace:", data["enlace"])
        print("Texto:", data["texto"])
        print("Anuncio:", "Sí" if data["anuncio"] else "No")
        print("Personas relacionadas:", ', '.join(data["personas_relacionadas"]))
    else:
        print("No se encontró ninguna publicación con ese ID.")

def actualizar():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["gran_san"]
    collection = db["publicaciones"]
    id_publicacion = input("Ingrese el ID de la publicación a actualizar: ")
    nuevo_texto = input("Ingrese el nuevo texto de la publicación: ")
    nuevo_anuncio = input("¿Es un anuncio? (Sí/No): ").lower() == 'sí'
    nuevas_personas_relacionadas = input("Ingrese las nuevas personas relacionadas a la publicación (separadas por comas): ").split(',')
    
    update_result = collection.update_one(
        {"id_publicacion": id_publicacion},
        {"$set": {
            "texto": nuevo_texto,
            "anuncio": nuevo_anuncio,
            "personas_relacionadas": nuevas_personas_relacionadas
        }}
    )
    if update_result.modified_count > 0:
        print("La publicación ha sido actualizada correctamente.")
    else:
        print("No se encontró ninguna publicación con ese ID.")

def eliminar():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["gran_san"]
    collection = db["publicaciones"]
    id_publicacion = input("Ingrese el ID de la publicación a eliminar: ")
    delete_result = collection.delete_one({"id_publicacion": id_publicacion})
    if delete_result.deleted_count > 0:
        print("La publicación ha sido eliminada correctamente.")
    else:
        print("No se encontró ninguna publicación con ese ID.")

def salir():
    print("¡Gracias por participar!")
    print("El programa se está cerrando...")
    exit()

def cargue():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["gran_san"]
    collection = db["publicaciones"]
    # Puedes insertar publicaciones iniciales aquí si lo deseas

op = menu()
cargue()
while True:
    if op == 1:
        crear()
    elif op == 2:
        consultar()
    elif op == 3:
        actualizar()
    elif op == 4:
        eliminar()
    elif op == 5:
        salir()
    else:
        print("Opción inválida, por favor seleccione una opción válida.")
    op = menu()
