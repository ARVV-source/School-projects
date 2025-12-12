class App {
  public static void main(String[] args) {
    Asistencia lista = new Asistencia();
    Student estudiante1 = new Student("Ilana Alva", "0272416");
    Student estudiante2 = new Student("Juan Perez", "1234567");
    lista.listaAlumnos.add(estudiante1);
    lista.listaAlumnos.add(estudiante2);
    lista.registrarLista();
  }
}
