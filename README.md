# challenge reglas yara ML
Realizacion del challenge de ML sobre reglas YARA
En este challenge se realizo un codigo en python para poder guardar reglas yara con su nombre, ejecutarlas, obtener los resultados y ver las guardadas o eliminarlas.
Se uso POST, GET, DELETE para interactuar mediante la API.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

URL de imagen DOCKER= https://hub.docker.com/repository/docker/emiperalta/imagenyaraemip

En este repositorio estara publicado el codigo source.

Consiste en:
---Create rule, en este endpoint se emplea una peticion POST donde se ingresa el nombre de la regla en "name" y en el campo "rule" se coloca la regla YARA en formato de STRING. Su url es ".../api/rule", este creara un diccionario dentro de una lista llamada DB, en la cual se generara secuencialmente su ID por diccionario.

---Rules created by user, este endpoint lee los diccionarios generados y almacenados en la lista DB, y los expone para poder observarlos. Se emplea un metodo GET. Su url es ".../api/rulescreated"

---Specific ID, este endpoint busca una regla creada por el usuario utilizando el ID y devuelve el diccionario en el que se encontro. Si no se encuentra devuelve un mensaje de error. Utilizandose un GET. Su url es ".../api/{id de la regla}"

---Delete rule, en este endpoint se elimina una rule creada por el usuario que se encuentre en la DB. Debiendo haber sido provisto el ID de la Rule a eliminar.

---Read current User, es un proceso de validacion donde se lee el usuario actual, siendo tanto la contraseña como el usuario hardcodeado (usuario:hireme, contraseña:plz)

---Aclaraciones importantes:

No pude usar YARA como extension de python, si bien indague en foros e incluso publique en el grupo oficial de YARA este problema no obtuve resolucion "https://groups.google.com/g/yara-project/c/gRWRGCSuwAo" como menciono en ese mensaje, incluso solicite ayuda en diferentes grupos de programadores, pero no obtuve respuesta debido a la baja frecuencia con la que yara es usada entre developer´s que conozco.

Si bien coloque el codigo como comentado dentro de main.py, quisiera agregar cosas:

-La compilacion y el salvaguardado de la regla deberian ocurrir cuando la regla se genera en el endpoint Create Rule, y guardarse en el buffer usando IO.

-En ambos Analyzer´s debe usarse las reglas guardadas en el buffer, no compilarse nuevamente, para esto se usara "x=yara.load(file="")" y se procedera como es habitue segun dicta la documentacion oficial de Yara.

-Yara puede analizar strings de texto, por eso se pasa como string dentro del buffer.

