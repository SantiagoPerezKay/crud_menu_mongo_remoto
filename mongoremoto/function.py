def muestra_campos(registro):
    for key in (registro):
       print(f" campo: {key} ")

def eleccionMenu():
    print("\n1: agregar registro")
    print("2: buscar registro")
    print("3: actualizar registro")
    print("4: eliminar registro")
    print("5: salir\n")

    menuOpcion=int(input("Ingrese opcion (numerica) para realizar una accion: "))
    return menuOpcion

 #se agregara un registro a la base remota en mongoatlas ,siempre y cuando se hayan ingresado correctamente los datos,sino largara un error
def agregarRegistro():
    print("**agregar registro**")
    try:
        idProduct=int(input ("Ingrese valor para idProduct: "))
        clase=input("ingrese valor para clase: ")
        nombre=input("ingrese valor para nombre: ")
        precio=int(input("ingrese valor para precio: "))
        date=datetime.datetime.now()
        productsTable.insert_one({'idProduct': idProduct, 'clase': clase, 'nombre': nombre, 'precio': precio, 'date': date})
    except:
         print("ha ocurrido un error")

def actualizarRegistro():
    
    idProduct=int(input("ingrese valor para idProduct: "))
    clase=input("ingrese valor para clase: ")
    nombre=input("ingrese valor para nombre: ")
    precio=int(input("ingrese valor para precio: "))
    date=input("ingrese valor para date: ")
    
    productsTable.update_one({"idProduct":idProduct},{"$set":{ "idProduct":idProduct,"clase":clase,"nombre":nombre,"precio":precio,"date":date}})
    