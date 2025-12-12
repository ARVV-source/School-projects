class Estudiante {
  private String numero;
  private String nombre;
  private String asistencia;

  Estudiante(String numero, String nombre) {
    this.numero = numero;
    this.nombre = nombre;
    this.asistencia = "Ausente";
  }

  String obtenerDatos() {
    return numero + ". | " + nombre + " | " + asistencia;
  }

  void marcarAsistencia() {
    if (asistencia.equals("Ausente")) {
      asistencia = "Presente";
    } else {
      asistencia = "Ausente";
    }
  }

  String getAsistencia() {
    return asistencia;
  }
}