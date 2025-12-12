import java.util.ArrayList;

class Asistencia {
  ArrayList<Student> listaAlumnos = new ArrayList<Student>();
  
  void registrarLista() {
    for (Student alumno : this.listaAlumnos) {
      alumno.asistencia = true;
      System.out.print("La asistencia de: " + alumno.nombre);
      System.out.println("a cambiado a " + alumno.asistencia);
    }        
  }
}