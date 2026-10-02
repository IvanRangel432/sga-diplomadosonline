from models import Alumno,Profesor,Notas

# CONFIGURACION PRINCIPAL DE LA PLATAFORMA 

# Se una activa una palanca que es (True) para que el sistema este activo
# De lo contrario cuando el usuario se salga, se activa False 


programa_en_curso= True

while programa_en_curso:

  # Menu Principal de Diplomados Online

 print("\n======================================")
 print("SGA-DO: SISTEMA DIPLOMADOS ONLINE")
 print("========================================")
 print("Opcion 1.Registrar Alumnos")
 print("Opcion 2.Registrar Profesor")
 print("Opcion 3.Registar Notas de un Alumno")
 print("Opcion 4.Deshacer Ultima Nota")
 print("Opcion 5.Generar cola de certificados")
 print("Opcion 6.Mostrar Reporte General")
 print("Opcion 7.Salir")
 print("=========================================")

 #Pedimos al usuario la opcion elegida en cuestion 
 opcion=input("Seleccione una opcion:")

 # Opcion 1 .Registrar Alumno
 if opcion == "1":
    print("---Usted ha seleccionado Registrar Estudiante---")
    
    cedula = input("Ingrese la Cédula de Identidad del Alumno: ").strip()
    nombre = input("Ingrese el Nombre Completo del Alumno: ").strip()
    correo = input("Ingrese el Correo Electrónico del Alumno: ").strip()
    tipo_programa = input("Ingrese el Programa Académico (Curso, Diplomado, Bootcamp): ").strip().capitalize()

    # Se instancia la clase Alumno
    nuevo_alumno = Alumno(cedula, nombre, correo, tipo_programa)

    # Se escribe en el archivo garantizando la coma final antes del salto de línea
    archivo_alumno = open("alumnos.txt", "a")
    archivo_alumno.write(f"{nuevo_alumno.cedula},{nuevo_alumno.nombre},{nuevo_alumno.correo},{nuevo_alumno.tipo_programa}\n")
    archivo_alumno.close()

    print("!Estudiante registrado con éxito¡")


    
  # Opcion 2. Registrar Profesor
   
 elif opcion == "2":
    print("---Usted ha seleccionado: Registrar Profesor---")

    nombre_profesor=input("Ingrese su nombre")
    cedula_profesor=input("Ingrese su Cedula de Identidad")
    correo_profesor=input("Ingrese su Correo Electronico")
    especialidad_materia=input("Ingrese su Especialidad y materia")

    # Usamos la clase Profesor

    nuevo_profesor=Profesor(nombre_profesor,cedula_profesor,especialidad_materia,correo_profesor)

    # Se guardan los datos en el archivo profesores.txt en modo "a"

    archivo_profesor=open("profesores.txt","a")
    archivo_profesor.write(f"{nuevo_profesor.nombre},{nuevo_profesor.cedula},{nuevo_profesor.correo},{nuevo_profesor.especialidad_materia}\n")
    archivo_profesor.close()

    print("!Se realizo con exito el ingreso de datos del Profesor¡")
    
    
 #Opcion 3. Registros de notas del Estudiante 
 elif opcion == "3":
    print("---Usted ha seleccionado Agregar Notas---")
    cedula_buscar = input("Ingrese la Cédula del alumno: ").strip()

    try:
        archivo = open("alumnos.txt", "r")
        lineas = archivo.readlines()
        archivo.close()

        encontrado = False
        nuevas_lineas = []

        for linea in lineas:
            linea_limpia = linea.strip()
            if not linea_limpia:
                continue

            datos = linea_limpia.split(",")
            
            if datos[0].strip() == cedula_buscar:
                encontrado = True
                cantidad = int(input("¿Cuántas notas desea ingresar?: "))
                
                lista_notas = []
                for i in range(cantidad):
                    nota = input(f"Ingrese la nota {i+1}: ").strip()
                    lista_notas.append(nota)

                # Si ya tenía notas previas, solo concatenamos con coma; si no, también agregamos coma
                str_notas = "," + ",".join(lista_notas)
                linea_actualizada = linea_limpia + str_notas + "\n"
                nuevas_lineas.append(linea_actualizada)
            else:
                nuevas_lineas.append(linea + "\n" if not linea.endswith("\n") else linea)

        if encontrado:
            archivo = open("alumnos.txt", "w")
            archivo.writelines(nuevas_lineas)
            archivo.close()
            print("!Notas agregadas con éxito!")
        else:
            print("Alumno no encontrado.")

    except FileNotFoundError:
        print("El archivo alumnos.txt no existe.")

 
 #Opcion 4. Deshacer ultimo registro de nota
 
 elif opcion == "4":
    print("---Usted ha seleccionado Deshacer Ultima Nota:---")

    ultima_nota_ = input("Ingrese su Cedula de Identidad para hacer el ultimo registro de nota:")

    archivo = open("alumnos.txt", "r")
    lineas = archivo.readlines()
    archivo.close()

    nuevas_lineas = []
    encontrado = False

    for linea in lineas:
      linea_limpia = linea.strip()
      if not linea_limpia:
        continue

      datos = linea_limpia.split(",")

      if datos[0] == ultima_nota_:
        encontrado = True
        # Los indices 0, 1, 2, 3 son Cedula, Nombre, Correo, Programa.
        # Si len(datos) > 4 significa que tiene notas guardadas.
        if len(datos) > 4:
          datos.pop() # Borra el último elemento (la última nota)
          linea_nueva = ",".join(datos) + "\n"
          nuevas_lineas.append(linea_nueva)
          print("!Ultima nota eliminada con exito¡")
        else:
          nuevas_lineas.append(linea_limpia + "\n")
          print("El alumno no tiene notas para borrar.")
      else:
        nuevas_lineas.append(linea_limpia + "\n")

    if not encontrado:
      print("No se encontro un alumno con esa cedula.")

    archivo = open("alumnos.txt", "w")
    archivo.writelines(nuevas_lineas)
    archivo.close()

    print("!Ultimo Registro de Nota Realizado con Exito")
   #Opcion 5. Generar Cola de Certificados 
 elif opcion == "5":
    print("---Usted ha seleccionado Generar cola de certificados---")
    cola_certificados = []

    try:
        archivo = open("alumnos.txt", "r")
        lineas = archivo.readlines()
        archivo.close()

        for linea in lineas:
            linea_limpia = linea.strip()
            if not linea_limpia:
                continue

            datos = [d.strip() for d in linea_limpia.split(",") if d.strip()]

            # Mínimo 5 elementos: Cédula, Nombre, Correo, Programa y al menos 1 Nota
            if len(datos) >= 5:
                cedula = datos[0]
                nombre = datos[1]
                programa = datos[3].capitalize()

                # Extraer todas las notas numéricas
                notas = [float(n) for n in datos[4:]]

                promedio = sum(notas) / len(notas)
                aprobado = False

                # Reglas de aprobación
                if programa == "Curso" and promedio >= 10:
                    aprobado = True
                elif programa == "Diplomado" and promedio >= 14:
                    aprobado = True
                elif programa == "Bootcamp":
                    if promedio >= 14 and all(n >= 14 for n in notas):
                        aprobado = True

                if aprobado:
                    cola_certificados.append([cedula, nombre, programa, promedio])

        # Se escribe directamente en el archivo certificados.txt
        reporte = open("certificados.txt", "w")
        reporte.write("=================================\n")
        reporte.write("          REPORTE GENERAL        \n")
        reporte.write("=================================\n")
        reporte.write(f"El total de graduandos en cola: {len(cola_certificados)}\n\n")

        numero = 1
        for alumno in cola_certificados:
            reporte.write(f"{numero}. [V-{alumno[0]}] {alumno[1]}\n")
            reporte.write(f"Programa: {alumno[2]}\n")
            reporte.write(f"-- Promedio Final: {alumno[3]:.2f}\n")
            reporte.write("==========================================\n")
            numero += 1

        reporte.write("-- Fin del reporte - Generado por el SGA -- \n")
        reporte.close()

        print(f"!Reporte Creado con éxito! Total en cola: {len(cola_certificados)}")

    except FileNotFoundError:
        print("El archivo alumnos.txt no existe.")
   #Opcion 6.Mostrar Reporte General 

 elif opcion== "6":
    print("=====================================================")
    print("                 REPORTE GENERAL SGA-DO              ")
    print("=====================================================")

    #LISTA DEL ESTATUS (PROFESORES)
    print("---LISTA DE PROFESORES ACTIVOS---")
    archivo_profesores=open("profesores.txt","r")
    lineas_profesores=archivo_profesores.readlines()
    archivo_profesores.close()

    for linea in lineas_profesores:
      linea_limpia=linea.replace("\n","")
      datos=linea_limpia.split(",")

      if len(datos) >=4:
        cedula_profesor=datos[1]
        nombre_profesor=datos[0]
        materia_profesor=datos[3]
        print(f"Profesor:{nombre_profesor},Cedula:{cedula_profesor},Estatus:Activo")

    #Lista de estatus (Alumnos)
    print("---LISTA DE ALUMNOS ACTIVOS---")
    archivo_alumno=open("alumnos.txt","r")
    lineas_alumno=archivo_alumno.readlines()
    archivo_alumno.close()

    for linea in lineas_alumno:
      linea_limpia=linea.replace("\n","")
      datos=linea_limpia.split(",")

      if len(datos) >=4:
        cedula_alum=datos[0]
        nombre_alum=datos[1]
        programa_alum=datos[3].capitalize()

       #Determinamos si en el estatus estan las notas ingresadas
        if len(datos)> 4:
         estatus="Con las notas ingresadas"
        else:
         estatus="Registradas (sin notas)"

        print(f"Cedula:V-{cedula_alum},Nombre:{nombre_alum},Programa:{programa_alum},Estatus:{estatus}")

    print("\n======================================================")
    print("              FIN DEL REPORTE                          ")
    print("=======================================================\n")

#Opcion 7. Salir 

 elif opcion == "7":
    print("--- Guardando cambios pendientes---")
    print("--- Limpiando memoria----")
    print("--- Hasta luego---")
    programa_en_curso = False