public class Models {
    public static class Persona {
        protected String nombre;
        protected String cedula;
        protected String correo;

        public Persona(String nombre, String cedula, String correo) {
            this.nombre = nombre;
            this.cedula = cedula;
            this.correo = correo;
        }

        public String obtenerDatosPersona() {
            return "Nombre: " + nombre + " | Cédula: " + cedula + " | Correo: " + correo;
        }
    }

    public static class Alumno extends Persona {
        private String programa_academico_alumno;

        public Alumno(String nombre, String cedula, String correo, String programa_academico_alumno) {
            super(nombre, cedula, correo);
            this.programa_academico_alumno = programa_academico_alumno;
        }

        public String mostrarInformacion() {
            return obtenerDatosPersona() + " | Programa Académico: " + programa_academico_alumno;
        }
    }
    
    public static class Profesor extends Persona {
        private String especialidad_materia;

        public Profesor(String nombre, String cedula, String correo, String especialidad_materia) {
            super(nombre, cedula, correo);
            this.especialidad_materia = especialidad_materia; 
        }

        public String mostrarInformacion() {
            return obtenerDatosPersona() + " | Especialidad: " + especialidad_materia;
        }
    }

    public static class Notas {
        private String cedula_encontrada;
        private double notas;

        public Notas(String cedula_encontrada, double notas) {
            this.cedula_encontrada = cedula_encontrada;
            this.notas = notas;
        }

        public void mostrar_notas() {
            System.out.println("Cédula: " + cedula_encontrada + " | Notas: " + notas);
        }
    }
}