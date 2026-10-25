import java.io.FileWriter;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.IOException;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.Stack;

public class Main {
    public static void main (String[] args){
        Scanner teclado = new Scanner (System.in);
        boolean programa_en_curso = true;
        
        // Pila para el control de notas (LIFO)
        Stack<String> pila_cedulas = new Stack<>();
        
        while (programa_en_curso){
            System.out.println("==================================================");
            System.out.println("============= SGA-DO DIPLOMADOS ONLINE ================= ");
            System.out.println("Ingrese una opcion");
            System.out.println("Opcion 1. Registrar Alumno");
            System.out.println("Opcion 2. Registrar Profesor");
            System.out.println("Opcion 3. Registrar Notas del Alumno");
            System.out.println("Opcion 4. Deshacer Ultima Nota del Alumno");
            System.out.println("Opcion 5. Generar Cola de Certificados ");
            System.out.println("Opcion 6. Mostrar Reporte General");
            System.out.println("Opcion 7. Salir");
            System.out.println("=====================================================");

            String opcion_seleccionada = teclado.nextLine().trim();

            // Opcion 1. Registrar Alumno 
            if (opcion_seleccionada.equals("1")){
                System.out.println("-------- Usted ha seleccionado Registrar Alumno --------");
                System.out.println("Ingrese su Cedula de Identidad:");
                String cedula_alumno = teclado.nextLine().trim();
                System.out.println("Ingrese su Nombre Completo:");
                String nombre_alumno = teclado.nextLine().trim();
                System.out.println("Ingrese su correo electronico:");
                String correo_alumno = teclado.nextLine().trim();
                System.out.println("Ingrese su Programa Academico (Curso, Diplomado, Bootcamp):");
                String programa_academico_alumno = teclado.nextLine().trim();
                
                // CORRECCIÓN: Guardar en formato CSV plano (cedula,nombre,correo,programa) para que las opciones 3, 5 y 6 lo lean bien
                try (BufferedWriter archivo_alumno = new BufferedWriter(new FileWriter("alumnos.txt", true))){
                    archivo_alumno.write(cedula_alumno + "," + nombre_alumno + "," + correo_alumno + "," + programa_academico_alumno);
                    archivo_alumno.newLine();
                    System.out.println("¡Estudiante registrado con éxito!");
                } catch (IOException e) {
                    System.out.println("Error al guardar los datos del alumno");
                }
            }
            // Opcion 2. Registrar Profesor 
            else if (opcion_seleccionada.equals("2")){
                System.out.println("------ Usted ha seleccionado Registrar Profesor ------");
                System.out.println("Ingrese su Cedula de Identidad:");
                String cedula_profesor = teclado.nextLine().trim();
                System.out.println("Ingrese su Nombre Completo:");
                String nombre_profesor = teclado.nextLine().trim();
                System.out.println("Ingrese su Correo Electronico:");
                String correo_profesor = teclado.nextLine().trim();
                System.out.println("Ingrese su Especialidad:");
                String especialidad_materia = teclado.nextLine().trim();
                
                // CORRECCIÓN: Guardar en formato CSV plano para el reporte de profesores
                try (BufferedWriter archivo_profesor = new BufferedWriter(new FileWriter("profesores.txt", true))){
                    archivo_profesor.write(cedula_profesor + "," + nombre_profesor + "," + correo_profesor + "," + especialidad_materia);
                    archivo_profesor.newLine();
                    System.out.println("¡Profesor registrado con éxito!");
                } catch (IOException e){
                    System.out.println("Error al ingresar los datos del profesor");
                }
            }
            // Opcion 3. Registrar Notas del Alumno
            else if (opcion_seleccionada.equals("3")){
                System.out.println("----- Usted ha seleccionado Registrar Notas del Alumno -----");
                System.out.println("Ingrese La Cedula del Alumno:");
                String cedula_buscar = teclado.nextLine().trim();

                ArrayList<String> lineas = new ArrayList<>();
                boolean encontrado = false;

                try (BufferedReader lector = new BufferedReader(new FileReader("alumnos.txt"))) {
                    String linea;
                    while ((linea = lector.readLine()) != null) {
                        lineas.add(linea);
                    }
                } catch (IOException e) {
                    System.out.println("El archivo alumnos.txt no existe o no se pudo leer.");
                    continue;
                }

                ArrayList<String> nuevas_lineas = new ArrayList<>();

                for (String linea : lineas) {
                    String linea_limpia = linea.trim();
                    if (linea_limpia.isEmpty()) continue;

                    String[] datos = linea_limpia.split(",");
                    
                    if (datos[0].trim().equals(cedula_buscar)) {
                        encontrado = true;
                        try {
                            System.out.print("¿Cuántas notas desea ingresar?: ");
                            int cantidad = Integer.parseInt(teclado.nextLine().trim());
                            
                            StringBuilder sbNotas = new StringBuilder();
                            for (int i = 0; i < cantidad; i++) {
                                System.out.print("Ingrese la nota " + (i + 1) + ": ");
                                String nota = teclado.nextLine().trim();
                                sbNotas.append(",").append(nota);
                            }

                            String linea_actualizada = linea_limpia + sbNotas.toString();
                            nuevas_lineas.add(linea_actualizada);
                        } catch (NumberFormatException e) {
                            System.out.println("Error: Debe ingresar un número entero válido.");
                            nuevas_lineas.add(linea_limpia);
                        }
                    } else {
                        nuevas_lineas.add(linea_limpia);
                    }
                }

                if (encontrado) {
                    try (BufferedWriter escritor = new BufferedWriter(new FileWriter("alumnos.txt", false))) {
                        for (String nl : nuevas_lineas) {
                            escritor.write(nl);
                            escritor.newLine();
                        }
                        pila_cedulas.push(cedula_buscar);
                        System.out.println("¡Notas agregadas con éxito!");
                    } catch (IOException e) {
                        System.out.println("Error al actualizar el archivo de alumnos.");
                    }
                } else {
                    System.out.println("Alumno no encontrado.");
                }
            }
            // Opcion 4. Deshacer Ultima Nota
            else if (opcion_seleccionada.equals("4")){
                System.out.println("----- Usted ha seleccionado Deshacer Ultima Nota -------");

                if (pila_cedulas.isEmpty()) {
                    System.out.println("No hay registros recientes de notas para deshacer en esta sesión.");
                } else {
                    String cedula_a_deshacer = pila_cedulas.pop();
                    System.out.println("Deshaciendo la última nota del alumno con cédula: " + cedula_a_deshacer);

                    ArrayList<String> lineas = new ArrayList<>();
                    try (BufferedReader lector = new BufferedReader(new FileReader("alumnos.txt"))) {
                        String linea;
                        while ((linea = lector.readLine()) != null) {
                            lineas.add(linea);
                        }
                    } catch (IOException e) {
                        System.out.println("El archivo alumnos.txt no existe.");
                        continue;
                    }

                    ArrayList<String> nuevas_lineas = new ArrayList<>();
                    boolean modificado = false;

                    for (String linea : lineas) {
                        String linea_limpia = linea.trim();
                        if (linea_limpia.isEmpty()) continue;

                        String[] datos = linea_limpia.split(",");

                        if (datos[0].trim().equals(cedula_a_deshacer)) {
                            if (datos.length > 4) {
                                StringBuilder sbReconstruido = new StringBuilder();
                                for (int i = 0; i < datos.length - 1; i++) {
                                    sbReconstruido.append(datos[i]);
                                    if (i < datos.length - 2) {
                                        sbReconstruido.append(",");
                                    }
                                }
                                nuevas_lineas.add(sbReconstruido.toString());
                                modificado = true;
                                System.out.println("¡Última nota eliminada con éxito!");
                            } else {
                                nuevas_lineas.add(linea_limpia);
                                System.out.println("El alumno no tiene notas para borrar.");
                            }
                        } else {
                            nuevas_lineas.add(linea_limpia);
                        }
                    }

                    if (modificado) {
                        try (BufferedWriter escritor = new BufferedWriter(new FileWriter("alumnos.txt", false))) {
                            for (String nl : nuevas_lineas) {
                                escritor.write(nl);
                                escritor.newLine();
                            }
                        } catch (IOException e) {
                            System.out.println("Error al actualizar el archivo.");
                        }
                    }
                }
            }
            // Opcion 5. Generar cola de Certificados 
            else if (opcion_seleccionada.equals("5")){
                System.out.println("------- Usted ha seleccionado Generar Cola de Certificados ---------");
                ArrayList<String> cola_certificados = new ArrayList<>();

                ArrayList<String> lineasCert = new ArrayList<>();
                try (BufferedReader lector = new BufferedReader(new FileReader("alumnos.txt"))) {
                    String linea;
                    while ((linea = lector.readLine()) != null) {
                        lineasCert.add(linea);
                    }
                } catch (IOException e) {
                    System.out.println("El archivo alumnos.txt no existe.");
                    continue;
                }

                for (String linea : lineasCert) {
                    String linea_limpia = linea.trim();
                    if (linea_limpia.isEmpty()) continue;

                    String[] datosBrutos = linea_limpia.split(",");
                    ArrayList<String> datos = new ArrayList<>();
                    for (String d : datosBrutos) {
                        if (!d.trim().isEmpty()) {
                            datos.add(d.trim());
                        }
                    }

                    if (datos.size() >= 4) {
                        String cedula = datos.get(0);
                        String nombre = datos.get(1);
                        String programa = datos.get(3).substring(0, 1).toUpperCase() + datos.get(3).substring(1).toLowerCase();

                        ArrayList<Double> notasList = new ArrayList<>();
                        boolean errorNotas = false;
                        for (int i = 4; i < datos.size(); i++) {
                            try {
                                notasList.add(Double.parseDouble(datos.get(i)));
                            } catch (NumberFormatException e) {
                                errorNotas = true;
                                break;
                            }
                        }
                        if (errorNotas) continue;

                        while (notasList.size() < 3) {
                            notasList.add(0.0);
                        }

                        double suma = 0;
                        for (double n : notasList) {
                            suma += n;
                        }
                        double promedio = suma / 3.0;
                        boolean aprobado = false;

                        if (programa.equals("Curso") && promedio >= 10) {
                            aprobado = true;
                        } else if (programa.equals("Diplomado") && promedio >= 14) {
                            aprobado = true;
                        } else if (programa.equals("Bootcamp")) {
                            boolean todasAltas = true;
                            for (double n : notasList) {
                                if (n < 14) {
                                    todasAltas = false;
                                    break;
                                }
                            }
                            if (todasAltas) {
                                aprobado = true;
                            }
                        }

                        if (aprobado) {
                            String detalle_estatus = programa.equals("Bootcamp") ? "APROBADO (Cumple regla de ninguna nota <14)" : "APROBADO";
                            cola_certificados.add(cedula + "," + nombre + "," + programa + "," + String.format("%.1f", promedio) + "," + detalle_estatus);
                        }
                    }
                }

                try (BufferedWriter reporte = new BufferedWriter(new FileWriter("certificados_pendientes.txt", false))) {
                    reporte.write("=========================================\n");
                    reporte.write("   REPORTE DE CERTIFICADOS PENDIENTES    \n");
                    reporte.write("=========================================\n");
                    reporte.write("Total de graduandos en cola: " + cola_certificados.size() + "\n\n");

                    int numero = 1;
                    for (String alumnoStr : cola_certificados) {
                        String[] alumno = alumnoStr.split(",");
                        reporte.write(numero + ". [" + alumno[0] + "] " + alumno[1] + "\n");
                        reporte.write("- Programa: " + alumno[2] + "\n");
                        reporte.write("- Promedio Final: " + alumno[3] + "\n");
                        reporte.write("- Estatus: " + alumno[4] + "\n");
                        reporte.write("=========================================\n");
                        numero++;
                    }
                    reporte.write("* Fin del reporte - Generado por SGA-DO *\n");
                    System.out.println("¡Reporte creado con éxito! Total de graduandos en cola: " + cola_certificados.size());
                } catch (IOException e) {
                    System.out.println("Error al generar el archivo de certificados.");
                }
            }
            // Opcion 6. Mostrar Reporte General
            else if (opcion_seleccionada.equals("6")){
                System.out.println("=====================================================");
                System.out.println("                 REPORTE GENERAL SGA-DO              ");
                System.out.println("=====================================================");

                System.out.println("---LISTA DE PROFESORES ACTIVOS---");
                try (BufferedReader lectorProf = new BufferedReader(new FileReader("profesores.txt"))) {
                    String linea;
                    while ((linea = lectorProf.readLine()) != null) {
                        String linea_limpia = linea.trim();
                        if (linea_limpia.isEmpty()) continue;
                        String[] datos = linea_limpia.split(",");

                        if (datos.length >= 4) {
                            String cedula_profesor = datos[0].trim();
                            String nombre_profesor = datos[1].trim();
                            System.out.println("Profesor: " + nombre_profesor + ", Cédula: " + cedula_profesor + ", Estatus: Activo");
                        }
                    }
                } catch (IOException e) {
                    System.out.println("El archivo profesores.txt no existe.");
                }

                System.out.println("\n---LISTA DE ALUMNOS ACTIVOS---");
                try (BufferedReader lectorAlum = new BufferedReader(new FileReader("alumnos.txt"))) {
                    String linea;
                    while ((linea = lectorAlum.readLine()) != null) {
                        String linea_limpia = linea.trim();
                        if (linea_limpia.isEmpty()) continue;
                        String[] datos = linea_limpia.split(",");

                        if (datos.length >= 4) {
                            String cedula_alum = datos[0].trim();
                            String nombre_alum = datos[1].trim();
                            String programa_alum = datos[3].trim();
                            if (!programa_alum.isEmpty()) {
                                programa_alum = programa_alum.substring(0, 1).toUpperCase() + programa_alum.substring(1).toLowerCase();
                            }

                            String estatus = (datos.length > 4) ? "Con las notas ingresadas" : "Registradas (sin notas)";

                            System.out.println("Cédula: " + cedula_alum + ", Nombre: " + nombre_alum + ", Programa: " + programa_alum + ", Estatus: " + estatus);
                        }
                    }
                } catch (IOException e) {
                    System.out.println("El archivo alumnos.txt no existe.");
                }

                System.out.println("\n======================================================");
                System.out.println("              FIN DEL REPORTE                          ");
                System.out.println("======================================================-\n");
            }
            // Opcion 7. Salir
            else if (opcion_seleccionada.equals("7")){
                System.out.println("----- Guardando cambios pendientes -------");
                System.out.println("----- Limpiando memoria -----");
                System.out.println("-- Hasta Luego --");
                programa_en_curso = false;
            } else {
                System.out.println("Opción no válida. Por favor, intente de nuevo.");
            }
        }
        teclado.close();
    }
}
