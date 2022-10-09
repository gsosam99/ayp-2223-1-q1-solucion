edificio={ "Marketing": [], "Recursos humanos": [], "Contabilidad": [], "Ventas": [], }
quit = False
cedulas = []

while quit == False:
  print("\n-------MENU-------\n")
  option = input("\nBienvenido.\nSeleccione una opción:\n1. Ingreso\n2. Salida\n3. Estadísticas\n4. Cerrar\n=> ")
  while ['1', '2', '3', '4'].count(option) == 0:
    print("\n-------MENU-------\n")
    option = input("\nIngreso inválido.\nSeleccione una opción:\n1. Ingreso\n2. Salida\n3. Estadísticas\n4. Cerrar\n=> ")

  if option == '1':
    print("\n-------INGRESO DE EMPLEADO-------\n")

    # PEDIMOS EL NOMBRE
    firstName = input("\nPor favor, ingrese el nombre del empleado: ")
    while not firstName.isalpha():
      firstName = input("\nIngreso inválido.\nPor favor, ingrese el nombre del empleado: ")

    # PEDIMOS EL APELLIDO
    lastName = input("\nPor favor, ingrese el apellido del empleado: ")
    while not lastName.isalpha():
      lastName = input("\nIngreso inválido.\nPor favor, ingrese el apellido del empleado: ")

    # PEDIMOS LA CÉDULA
    ci = input("\nPor favor, ingrese el documento de identidad del empleado: ")
    while not ci.isnumeric():
      ci = input("\nIngreso inválido.\nPor favor, ingrese el documento de identidad del empleado sin puntos ni letras: ")
    while ci in cedulas:
      ci = input("\nIngreso inválido.\nUna persona con esta cédula de identidad ya se encuentra en el edificio. Ingrese el documento de identidad del empleado:  ")
    cedulas.append(ci)

    # PEDIMOS LA EDAD
    age = input("\nPor favor, ingrese la edad del empleado: ")
    while not age.isnumeric() or int(age) < 0:
      age = input("\nIngreso inválido.\nPor favor, ingrese la edad del empleado: ")

    person = {"Nombre": firstName, "Apellido": lastName, "Edad": int(age), "CI": ci}

    # PEDIMOS EL DEPARTAMENTO
    department = input("\nPor favor, \nSeleccione el número de uno de los siguientes departamentos:\n1. Marketing\n2. Recursos humanos\n3. Contabilidad\n4. Ventas\n=> ")
    while department not in ['1', '2', '3', '4']:
      department = input("\nIngreso inválido.\nPor favor, \nSeleccione el número de uno de los siguientes departamentos:\n1. Marketing\n2. Recursos humanos\n3. Contabilidad\n4. Ventas\n=> ")

    # AGREGAMOS A LA PERSONA A LA LISTA DEL DEPARTAMENTO
    if department == '1':
      edificio["Marketing"].append(person)
    elif department == '2':
      edificio["Recursos humanos"].append(person)
    elif department == '3':
      edificio["Contabilidad"].append(person)
    else:
      edificio["Ventas"].append(person)

  elif option == '2':
    print("\n-------SALIDA DE EMPLEADO-------\n")
    # Primero hay que revisar si la base de datos esta vacía ya que no se pueden salir personas si no hay nadie dentro del edificio
    if len(edificio["Marketing"]) == 0 and len(edificio["Recursos humanos"]) == 0 and len(edificio["Contabilidad"]) == 0 and len(edificio["Ventas"]) == 0:
      print("\nNo hay nadie en el edificio. Serás redireccionado al menu\n")
    else :
     # Mostramos por pantalla las personas que se encuentran en el edificio
      for department in edificio:
        if len(edificio[department]) != 0:
          print(f"\nDepartamento de {department}")
          for employee in edificio[department]:
            print(employee["Nombre"] + " " + employee["Apellido"] + ": " + employee["CI"])

      delete = input("\nSeleccione el número de cédula de la persona que desea salir del edificio\n=> ")
      while delete not in cedulas:
        delete = input(f"Ingreso invalido, la persona con cédula de identidad {delete} no existe.\nSeleccione el número de cédula de la persona que desea salir del edificio\n=> ")

      for department in edificio:
        for employee in edificio[department]:
          if employee["CI"] == delete:
            edificio[department].remove(employee)
      cedulas.remove(delete)


  elif option == '3':
    print("\n-------MOSTRAR ESTADÍSTICAS-------\n")
    # Primero hay que revisar si la base de datos esta vacía ya que no se pueden salir personas si no hay nadie dentro del edificio
    if len(edificio["Marketing"]) == 0 and len(edificio["Recursos humanos"]) == 0 and len(edificio["Contabilidad"]) == 0 and len(edificio["Ventas"]) == 0:
      print("\nNo hay nadie en el edificio. Serás redireccionado al menu\n")
    else:
      # NUMERO DE PERSONAS POR DEPARTAMENTO
      mTotal = len(edificio["Marketing"])
      rTotal = len(edificio["Recursos humanos"])
      cTotal = len(edificio["Contabilidad"])
      vTotal = len(edificio["Ventas"])

      print(f"\nEn el departamento de Marketing hay {mTotal} persona(s)\nEn el departamento de Recursos humanos hay {rTotal} persona(s)\nEn el departamento de Contabilidad hay {cTotal} persona(s)\nEn el departamento de Ventas hay {vTotal} persona(s)")

      # NUMERO DE PERSONAS EN EL EDIFICIO
      total = mTotal + rTotal + cTotal + vTotal
      print(f"\nHay {total} persona(s) en el edificio")

      # BONO: PROMEDIO DE EDAD POR DEPARTAMENTO
      mAges = 0
      rAges = 0
      cAges = 0
      vAges = 0

      for employee in edificio["Marketing"]:
        mAges += employee["Edad"]
      if len(edificio["Marketing"]) == 0:
        mPromedio = 0
      else:
        mPromedio = mAges/mTotal
      print(f"\nEl promedio de edad en el departamento de Marketing es {mPromedio}")

      for employee in edificio["Recursos humanos"]:
        rAges += employee["Edad"]
      if len(edificio["Recursos humanos"]) == 0:
        rPromedio = 0
      else:
        rPromedio = rAges/rTotal
      print(f"El promedio de edad en el departamento de Recursos humanos es {rPromedio}")

      for employee in edificio["Contabilidad"]:
        cAges += employee["Edad"]
      if len(edificio["Contabilidad"]) == 0:
        cPromedio = 0
      else:
        cPromedio = cAges/cTotal
      print(f"El promedio de edad en el departamento de Contabilidad es {cPromedio}")

      for employee in edificio["Ventas"]:
        vAges += employee["Edad"]
      if len(edificio["Ventas"]) == 0:
        vPromedio = 0
      else:
        vPromedio = vAges/vTotal
      print(f"El promedio de edad en el departamento de Ventas es {vPromedio}")

      # BONO: PROMEDIO DE EDAD EN EL EDIFICIO
      promedio = (mAges + rAges + cAges + vAges) / total
      print(f"\nEl promedio de edad en el edificio es {promedio}")

  else:
    quit = True
print("\nAdios, gracias por este servicio")
