from models import Alumno, Profesor, Notas

# CONFIGURACION PRINCIPAL DE LA PLATAFORMA 
programa_en_curso = True

while programa_en_curso:

    # Menu Principal de Diplomados Online
    print("\n======================================")
    print("SGA-DO: SISTEMA DIPLOMADOS ONLINE")
    print("========================================")
    print("Opcion 1. Registrar Alumnos")
    print("Opcion 2. Registrar Profesor")
    print("Opcion 3. Registrar Notas de un Alumno")
    print("Opcion 4. Deshacer Ultima Nota")
    print("Opcion 5. Generar cola de certificados")
    print("Opcion 6. Mostrar Reporte General")
    print("Opcion 7. Salir")
    print("=========================================")

    opcion = input("Seleccione una opcion: ").strip()

    # Opcion 1. Registrar Alumno
    if opcion == "1":
        print("---Usted ha seleccionado Registrar Estudiante---")
        
        cedula = input("Ingrese la Cédula de Identidad del Alumno: ").strip()
        nombre = input("Ingrese el Nombre Completo del Alumno: ").strip()
        correo = input("Ingrese el Correo Electrónico del Alumno: ").strip()
        tipo_programa = input("Ingrese el Programa Académico (Curso, Diplomado, Bootcamp): ").strip().capitalize()

        nuevo_alumno = Alumno(cedula, nombre, correo, tipo_programa)

        with open("alumnos.txt", "a") as archivo_alumno:
            archivo_alumno.write(f"{nuevo_alumno.cedula},{nuevo_alumno.nombre},{nuevo_alumno.correo},{nuevo_alumno.tipo_programa}\n")

        print("¡Estudiante registrado con éxito!")

    # Opcion 2. Registrar Profesor
    elif opcion == "2":
        print("---Usted ha seleccionado: Registrar Profesor---")

        cedula_profesor = input("Ingrese su Cédula de Identidad: ").strip()
        nombre_profesor = input("Ingrese su Nombre Completo: ").strip()
        correo_profesor = input("Ingrese su Correo Electrónico: ").strip()
        especialidad_materia = input("Ingrese su Especialidad y materia: ").strip()

        nuevo_profesor = Profesor(cedula_profesor, nombre_profesor, correo_profesor, especialidad_materia)

        with open("profesores.txt", "a") as archivo_profesor:
            archivo_profesor.write(f"{nuevo_profesor.cedula},{nuevo_profesor.nombre},{nuevo_profesor.correo},{nuevo_profesor.especialidad_materia}\n")

        print("¡Se realizó con éxito el ingreso de datos del Profesor!")
        
    # Opcion 3. Registros de notas del Estudiante 
    elif opcion == "3":
        print("---Usted ha seleccionado Agregar Notas---")
        cedula_buscar = input("Ingrese la Cédula del alumno: ").strip()

        try:
            with open("alumnos.txt", "r") as archivo:
                lineas = archivo.readlines()

            encontrado = False
            nuevas_lineas = []

            for linea in lineas:
                linea_limpia = linea.strip()
                if not linea_limpia:
                    continue

                datos = linea_limpia.split(",")
                
                if datos[0].strip() == cedula_buscar:
                    encontrado = True
                    try:
                        cantidad = int(input("¿Cuántas notas desea ingresar?: "))
                        lista_notas = []
                        for i in range(cantidad):
                            nota = input(f"Ingrese la nota {i+1}: ").strip()
                            lista_notas.append(nota)

                        str_notas = "," + ",".join(lista_notas)
                        linea_actualizada = linea_limpia + str_notas + "\n"
                        nuevas_lineas.append(linea_actualizada)
                    except ValueError:
                        print("Error: Debe ingresar un número entero válido para la cantidad de notas.")
                        nuevas_lineas.append(linea if linea.endswith("\n") else linea + "\n")
                else:
                    nuevas_lineas.append(linea if linea.endswith("\n") else linea + "\n")

            if encontrado:
                with open("alumnos.txt", "w") as archivo:
                    archivo.writelines(nuevas_lineas)
                print("¡Notas agregadas con éxito!")
            else:
                print("Alumno no encontrado.")

        except FileNotFoundError:
            print("El archivo alumnos.txt no existe.")

    # Opcion 4. Deshacer ultimo registro de nota
    elif opcion == "4":
        print("---Usted ha seleccionado Deshacer Última Nota---")
        ultima_nota_ = input("Ingrese la Cédula del alumno para deshacer nota: ").strip()

        try:
            with open("alumnos.txt", "r") as archivo:
                lineas = archivo.readlines()

            nuevas_lineas = []
            encontrado = False
            modificado = False

            for linea in lineas:
                linea_limpia = linea.strip()
                if not linea_limpia:
                    continue

                datos = linea_limpia.split(",")

                if datos[0].strip() == ultima_nota_:
                    encontrado = True
                    if len(datos) > 4:
                        datos.pop()
                        linea_nueva = ",".join(datos) + "\n"
                        nuevas_lineas.append(linea_nueva)
                        modificado = True
                        print("¡Última nota eliminada con éxito!")
                    else:
                        nuevas_lineas.append(linea_limpia + "\n")
                        print("El alumno no tiene notas para borrar.")
                else:
                    nuevas_lineas.append(linea_limpia + "\n")

            if encontrado and modificado:
                with open("alumnos.txt", "w") as archivo:
                    archivo.writelines(nuevas_lineas)
            elif not encontrado:
                print("No se encontró un alumno con esa cédula.")

        except FileNotFoundError:
            print("El archivo alumnos.txt no existe.")

    # Opcion 5. Generar Cola de Certificados 
    elif opcion == "5":
        print("---Usted ha seleccionado Generar cola de certificados---")
        cola_certificados = []

        try:
            with open("alumnos.txt", "r") as archivo:
                lineas = archivo.readlines()

            for linea in lineas:
                linea_limpia = linea.strip()
                if not linea_limpia:
                    continue

                datos = [d.strip() for d in linea_limpia.split(",") if d.strip()]

                if len(datos) >= 4:
                    cedula = datos[0]
                    nombre = datos[1]
                    programa = datos[3].capitalize()

                    try:
                        notas = [float(n) for n in datos[4:]]
                    except ValueError:
                        continue

                    while len(notas)< 3:
                        notas.append(0.0)

                    promedio = sum(notas) / 3.0
                    aprobado = False
                    

                    if programa == "Curso" and promedio >= 10:
                        aprobado = True
                    elif programa == "Diplomado" and promedio >= 14:
                        aprobado = True
                    elif programa == "Bootcamp":
                        if all(n >= 14 for n in notas):
                            aprobado = True
                           
                    if aprobado:
                        detalle_estatus="APROBADO (Cumple regla de ninguna nota <14)" if programa == "Bootcamp" else "APROBADO"
                        cola_certificados.append([cedula, nombre, programa, promedio, detalle_estatus])

            with open("certificados_pendientes.txt", "w") as reporte:
                reporte.write("=========================================\n")
                reporte.write("   REPORTE DE CERTIFICADOS PENDIENTES    \n")
                reporte.write("=========================================\n")
                reporte.write(f"Total de graduandos en cola: {len(cola_certificados)}\n\n")

                numero = 1
                for alumno in cola_certificados:
                    reporte.write(f"{numero}. [{alumno[0]}] {alumno[1]}\n")
                    reporte.write(f"- Programa: {alumno[2]}\n")
                    reporte.write(f"- Promedio Final: {alumno[3]:.1f}\n")
                    reporte.write(f"- Estatus: {alumno[4]}\n")
                    reporte.write("=========================================\n")
                    numero += 1

                reporte.write("* Fin del reporte - Generado por SGA-DO *\n")

            print(f"¡Reporte creado con éxito! Total de graduandos en cola: {len(cola_certificados)}")

        except FileNotFoundError:
            print("El archivo alumnos.txt no existe.")

    # Opcion 6. Mostrar Reporte General 
    elif opcion == "6":
        print("=====================================================")
        print("                 REPORTE GENERAL SGA-DO              ")
        print("=====================================================")

        print("---LISTA DE PROFESORES ACTIVOS---")
        try:
            with open("profesores.txt", "r") as archivo_profesores:
                for linea in archivo_profesores:
                    linea_limpia = linea.strip()
                    if not linea_limpia:
                        continue
                    datos = linea_limpia.split(",")

                    if len(datos) >= 4:
                        cedula_profesor = datos[0]
                        nombre_profesor = datos[1]
                        print(f"Profesor: {nombre_profesor}, Cédula: {cedula_profesor}, Estatus: Activo")
        except FileNotFoundError:
            print("El archivo profesores.txt no existe.")

        print("\n---LISTA DE ALUMNOS ACTIVOS---")
        try:
            with open("alumnos.txt", "r") as archivo_alumno:
                for linea in archivo_alumno:
                    linea_limpia = linea.strip()
                    if not linea_limpia:
                        continue
                    datos = linea_limpia.split(",")

                    if len(datos) >= 4:
                        cedula_alum = datos[0]
                        nombre_alum = datos[1]
                        programa_alum = datos[3].capitalize()

                        if len(datos) > 4:
                            estatus = "Con las notas ingresadas"
                        else:
                            estatus = "Registradas (sin notas)"

                        print(f"Cédula: V-{cedula_alum}, Nombre: {nombre_alum}, Programa: {programa_alum}, Estatus: {estatus}")
        except FileNotFoundError:
            print("El archivo alumnos.txt no existe.")

        print("\n======================================================")
        print("              FIN DEL REPORTE                          ")
        print("=======================================================\n")

    # Opcion 7. Salir 
    elif opcion == "7":
        print("--- Guardando cambios pendientes ---")
        print("--- Limpiando memoria ---")
        print("--- Hasta luego ---")
        programa_en_curso = False