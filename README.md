# Quiz-I
## Problema 1 (3pts):
Twitter te ha contratado para que desarrolles un algoritmo en Python que permita censurar tweets. Debes tomar por teclado la oración a censurar y el caracter por el que deseas reemplazar las letras de esas palabras censuradas (dadas en una lista), y mostrar en pantalla la oración censurada.

palabras_censuradas=["racismo", "terrorista", "peligro", "miedo", "odio"]

### Ejemplo de input:
	> "En nuestro país hay un terrorista, es un peligro para la sociedad. Las personas tienen mucho miedo."
	> "*"
### Output esperado:
	> En nuestro país hay un ********** es un ******* para la sociedad. Las personas tienen mucho *****.


## Problema 2 (17pts + 3pts):
Te han contratado para que diseñes un algoritmo en Python que lleve el registro de las entradas y salidas de los empleados de una compañía a los distintos departamentos del edificio. Dichos departamentos se encuentran reflejados en el siguiente diccionario:
  
edificio={
   "Marketing": [],
   "Recursos humanos": [],
   "Contabilidad": [],
   "Ventas": [],
}

El software debe contar con estas funcionalidades:

- **Ingreso al edificio:** Se requiere agregar a la base de datos planteada anteriormente los datos de la persona que está entrando al edificio (nombre, apellido, edad y cédula). Los datos de esta persona deben ubicarse dentro de la lista correspondiente al departamento al que se dirija. 

  Por ejemplo, si Pedro Pérez entra al edificio y se dirige al departamento de marketing, el diccionario se vería así:

  edificio={
      "Marketing": [ { “Nombre”: “Pedro”, “Apellido”: “Pérez", “Edad”: 24, “Cédula”: 26123456 }, ],
      "Recursos humanos": [],
      "Contabilidad": [],
      "Ventas": [],
  }

  *RECORDATORIO: Las cédulas de identidad son únicas para cada persona, por ende, no pueden haber dos personas o más con la misma cédula dentro del edificio.*

- **Salida del edificio:** Se requiere eliminar a la persona que se desee de la lista en la que se encuentra.

  *TIP: Para eliminar a una persona en particular, hacerlo ingresando algún valor que sea único de esa persona.*

- **Estadísticas:** Se requiere mostrar por pantalla en un output amigable e intuitivo al usuario las siguientes estadísticas:
  - Cuántas personas hay en cada departamento.
  - Cuántas hay en total en el edificio.
  - **BONO (3 puntos extras. 1.5 c/u):**
    - Cuál es el promedio de edad de las personas en cada departamento.
    - Cuál es el promedio de edad de las personas en el edificio. 

### REQUERIMIENTOS DEL ALGORITMO

- Contar con un menú que permita al usuario seleccionar la acción a realizar.
- Validar inputs: 
  - El nombre y el apellido deben ser de tipo string con solo caracteres alfabéticos.
  - La cédula y la edad debe tener solo caracteres numéricos y enteros.
  - Y cualquier otro input utilizado debe ser tolerante a ingresos inválidos.
- Volver al menú inicial al finalizar cada operación, y permitir al usuario cerrar el programa cuando lo desee.
