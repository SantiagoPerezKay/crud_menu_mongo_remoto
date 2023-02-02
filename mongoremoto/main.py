"""
programa donde se utiliza las funciones basicas como ingresar,buscar,actualizar,borrar,indexar,contar,etc a un registro en una BD mongo utilizando la libreria pymongo"
"""
from pymongo import MongoClient
import datetime
import function

try:
        client = MongoClient("mongodb+srv://admin:admin@cluster0.dm9lnki.mongodb.net/?retryWrites=true&w=majority").test
        #instancio un objeto de MongoClient con parametros de mongo Atlas (remoto)
        productsTable=client["products"]
        print("conexion a mongo atlas/base de datos 'test' exitosa")
except:
       
        print("no se pudo conectar a  MongoAtlas")

        
print("la coleccion/tabla contiene: ",productsTable.count_documents({}),"registros")
print("ejemplo de registros en la coleccion 'products'")
ejemplo=productsTable.find_one({})
print(productsTable.find_one({}),"\n")
#obtengo 1 elemento para poder recorrer sus keys y mostrarlas por pantalla
    
     #funcion que muestra los campos del registro  
menuOpcion=1
while menuOpcion >0 and menuOpcion<5:
        menuOpcion=function.eleccionMenu()
        #funcion que muestra un menu que solicita y guarda su valor para realizar una accion determinada
        if menuOpcion==1:
             function.agregarRegistro() 

        elif menuOpcion==2:
               #se buscara un registro segun el campo indicado (se mostrara por defecto el 1ero si son varios)
                print("\n**buscar registro**")        
                function.muestra_campos(ejemplo)  
                buscar=input("Ingrese por el campo desea buscar un registro: ")
                valorOPcion=input("ingrese valor para la busqueda: ")

                if buscar.lower()=="_id":
                        print("BUSQUEDA POR CODIGO")
                        print("\n",productsTable.find_one({"_id" : valorOPcion }))

                if buscar.lower()=="idproduct":
                        print("ELIGIO BUSSQUEDA POR ID")
                        print("\n",productsTable.find_one({"idProduct" : valorOPcion }))

                if buscar.lower()=="clase":      
                        print("ELIGIO BUSSQUEDA CLASE")
                        print("\n",productsTable.find_one({"clase" : valorOPcion }))

                if buscar.lower()=="nombre":      
                        print("ELIGIO BUSSQUEDA NOMBRE")
                        print("\n",productsTable.find_one({"nombre" : valorOPcion }))

                if buscar.lower()=="precio":    
                        print("ELIGIO BUSSQUEDA PRECIO")
                        print("\n",productsTable.find_one({"precio" : valorOPcion }))

                if buscar.lower()=="date":      
                        print("ELIGIO BUSSQUEDA PRECIO")
                        print("\n",productsTable.find_one({"date" : valorOPcion }))
                


        elif menuOpcion==3:

                print("**actualizar registro por idproduct**\n")   
               
                function.actualizarRegistro()
               
        elif menuOpcion==4:
                print("**eliminar registro\n")        
                idProduct=int(input("ingrese valor para eliminar por idProduct: "))
                print(productsTable.find_one({"idProduct" : idProduct }),"\n")
                opcion=input("seguro de que desea eliminar este registro? S/N")
                if opcion.upper()=="S": 
                        productsTable.delete_one({"idProduct":idProduct})

        elif menuOpcion==5:
                print("**opcion salir**")
                break
        else:
                print("opcion incorrecta")
        

print("programa finalizado")

"""

db = client['personasDB']#creo base de datos con nombre "personas"
tablaPersonas=db["personas"]
persona1 = {"_id":1,
                "nombre": "santiago",
                "apellido": "My first blog post!",
                "edad": 25,
                "date": datetime.datetime.utcnow()}
persona2 = {"_id":2,
                "nombre": "santiagoaaaaaaaaaaaaaaaaaaaaa",
                "apellido": "My seconds blog post!",
                "edad": 35,
                "date": datetime.datetime.utcnow()} 
persona3 = {"_id":3,
                "nombre": "robertototo",
                "apellido": "juarez",
                "edad": 27,
                "date": datetime.datetime.utcnow()}
persona4 = {"_id":4,
                "nombre": "gaston",
                "apellido": "gimenez",
                "edad": 35,
                "date": datetime.datetime.utcnow()} 

#********************EJEMPLO CONTAR REGISTRO***********************#

print("la coleccion contiene: ",tablaPersonas.count_documents({}),"registros")
#Muestro cantidad de registros

#********************EJEMPLOS DE INSERTAR DATOS***********************#

#tablaPersonas.insert_one({"_id":4,"nombre":"Diego","edad": 42,"date": datetime.datetime.utcnow()})
#Inserto un registro ,indicando key y value.
#tablaPersonas.insert_many([persona1,persona2,persona3,persona4])
#inserto 3 personas a la vez a la base de mongo con id definido

#*************************************EJEMPLOS DE BUSQUEDA****************************#

busqueda=tablaPersonas.find({})
#creo un objeto iterable con la busqueda de registros en la tabla/collection tablaPersonas para recorrelo
print("\nregistros de la coleccion tablaPersonas:")
for element in busqueda:
#recorro el objeto iterable
        print(element)
print("\nla 1era persona con 35 de edad es:")
busquedaEdad=tablaPersonas.find_one({"edad":35})
#hago una consulta para encontrar 1 solo registro por mas que haya mas campos con el mismo valor
print(busquedaEdad)
print("\nregistro con _id 3:")
busquedaId=tablaPersonas.find({"_id":3})#una forma mas rebuscada en ves de usar find_one
##hago una consulta para encontrar 1 solo registro ya que el campo "_id" en mongo es el campo clave y solo habra un unico valor en cada registro
print(busquedaId[0])#al devolver un objeto iterable(aunque contenga 1 solo valor) ,especifico la posición 0 para el 1er elemento.
busquedaId=tablaPersonas.find({"_id":3})

#*************************************EJEMPLO DE UPDATE*********************************#
print("se actualiza una sola persona con ID =2")
tablaPersonas.update_one( { '_id': 2 },{ "$set": { 'nombre': "julianAlvarez" } })
#se actuliza un unico registro con _id =2 el campo nombre :"valor",en caso de que no coincida el campo se me crea un nuevo campo
print("\n",tablaPersonas.find_one({"_id":2}))

print("\nse actualiza las personas con edad 35:")
tablaPersonas.update_one( { 'edad': 35 },{ "$set": { 'edad': 88 } })
#se actuliza un unico registro con _id =2 el campo nombre :"valor",en caso de que no coincidiera el campo se  crea un nuevo campo
listaDeActualizados=tablaPersonas.find({"edad":88})
for element in listaDeActualizados:
        print(element)
print("se incrementa la edad del _id 2: ")
tablaPersonas.update_one( { '_id': 2 },{ '$inc': { 'edad': 10 } })#con "$inc" se incrementa el valor
print("\n",tablaPersonas.find_one({'_id':2}),"\n")

#*************************************EJEMPLO DE DELETE*********************************#

tablaPersonas.delete_one({"_id":4})
#se elimina el registro con _id =4 en la coleccion tablaPersonas yse muestra todos los registros
nuevaTabla=tablaPersonas.find({})
for persona in nuevaTabla:
        print(persona)

"""