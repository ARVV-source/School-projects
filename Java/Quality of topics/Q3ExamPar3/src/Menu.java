import java.util.Scanner;

class Menu {
  private Lista tareaManager;
  private Scanner scanner;
  private String opcion;

  Menu() {
    tareaManager = new Lista();
    scanner = new Scanner(System.in);
  }

  private void mostrarOpciones() {
    System.out.println("\n========== Control de Asistencia ==========");
    System.out.println("1. Registrar nuevo estudiante");
    System.out.println("2. Ver pase de lista");
    System.out.println("3. Marcar asistencia de estudiante");
    System.out.println("4. Eliminar estudiante del registro");
    System.out.println("5. Salir del sistema");
    System.out.println("Seleccione una opcion: ");
  }

  private void procesarOpcion(String opcion) {
    switch (opcion.trim()) {
      case "1":
        tareaManager.crearestudiante();
        break;
      case "2":
        tareaManager.mostrarPasedeLista();
        break;
      case "3":
        tareaManager.actualizarEstado();
        break;
      case "4":
        tareaManager.eliminarestudiante();
        break;
      case "5":
        System.out.println("Saliendo del sistema de control de asistencia...");
        return;
      default:
        System.out.println("Opcion no valida, intente nuevamente");
        break;
    }
  }

  void ejecutar() {
    while (true) {
      mostrarOpciones();
      opcion = scanner.nextLine();
      if (opcion.equals("5")) {
        break;
      }
      procesarOpcion(opcion);
      System.out.println(" ");
    }
  }
}
