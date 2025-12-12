import java.util.Scanner;

class Menu {
  private String funcion;
  private Tarea tarea;
  private Scanner sc;

  Menu() {
    tarea = new Tarea();
    sc = new Scanner(System.in);
  }

  Menu(int z) {
    System.out.println("Ejemplo innecesario de overloading");
    tarea = new Tarea();
    sc = new Scanner(System.in);
  }

  void iniciarMenu() {
    System.out.println("=== Bienvenido al sistema de Pendientes ===");
    System.out.println("Ingrese el menu al que desea ingresar");
    System.out.println("1. Agregar tarea a la lista");
    System.out.println("2. Ver la lista de tareas");
    System.out.println("3. Cambiar estado de una tarea");
    System.out.println("4. Borrar una tarea");
    System.out.println("5. Salir del sistema");
    System.out.println(" ");
    System.out.println(" ");
    funcion = sc.nextLine();
    System.out.println(" ");
    System.out.println(" ");
    switch (funcion) {
      case "1":
        tarea.añadirTarea();
        System.out.println(" ");
        System.out.println(" ");
        break;
      case "2":
        tarea.verTareas();
        System.out.println(" ");
        System.out.println(" ");
        break;
      case "3":
        tarea.cambioEstado();
        System.out.println(" ");
        System.out.println(" ");
        break;
      case "4":
        tarea.borrarTarea();
        System.out.println(" ");
        System.out.println(" ");
        break;
      case "5":
        return;
      default:
        System.out.println("Opcion invalida ingrese una opcion valida");
        System.out.println(" ");
        System.out.println(" ");
        break;
    }
    iniciarMenu();
  }
}
