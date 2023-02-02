# crud_menu_mongo_remoto

###### #### programa con un menu que se muestra por consola,donde se pueden realizar las acciones basicas con una base de datos (CRUD),hacia una base de datos no relacional remota (mongoDBATLAS).

### librerias utilizadas
1. from pymongo import MongoClient
Para realizar la conexion hacia el cliente de mongo y realizar las acciones a un BD
2. datetime
para obtener el tiempo actual

**menu**


- agregar registro:
Solo se contemplo la accion de ingresar un registro por ves,indicando sus valores para cada campo.

- buscar registro:
Busca un registro por la key y value ingresada por el usuario,sino hay coincidencia se retornara un none.

- actualizar registro:
Se solicita ingresar un value para idProduct,para realizar la busqueda sobre el campo donde se ermitira actualizar un registro,cargando todos los valores nuevamente para este registro.

- eliminar registro:
Se solicita ingresar un value para el campo idProduct,para eliminar el registro completo.El usuario debera corrobar si desea realizar la eliminación o no.

- salir:
Finalizara la ejecucion del programa
