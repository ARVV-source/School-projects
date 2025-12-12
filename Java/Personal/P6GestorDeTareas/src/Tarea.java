import java.util.ArrayList;
import java.util.Scanner;

class Tarea {
  private ArrayList<String[][]> lista;
  private String[][] tarea;
  private Scanner sc;

  Tarea() {
    lista = new ArrayList<String[][]>();
    tarea = new String[4][1];
    sc = new Scanner(System.in);
  }

  void verTareas() {
    if (lista.size() < 1) {
      System.out.println("=============== Listado de tareas ===============");
      System.out.println("Actualmente no cuentas con tareas en tu listado");
    } else {
      System.out.println("=============== Listado de tareas ===============");
      for (String[][] x : lista) {
        System.out.println(x[0][0] + ". | " + x[1][0] + " | " + x[2][0] + " | " + x[3][0]);
      }
    }
  }

  void añadirTarea() {
    String numTarea = String.valueOf(lista.size() + 1);
    tarea = new String[4][1];
    tarea[0][0] = numTarea;
    System.out.println("Ingrese el nombre de su tarea.");
    String nomTarea = sc.nextLine();
    tarea[1][0] = nomTarea;
    System.out.println("Describa su tarea.");
    String desctarea = sc.nextLine();
    tarea[2][0] = desctarea;
    String estado = "Pendiente";
    tarea[3][0] = estado;
    lista.add(tarea);
  }

  void cambioEstado() {
    System.out.print("Ingrese el numero de la tarea a");
    System.out.println(" la cual le desea hacer el cambio de estado.");
    System.out.println(" ");
    int indice = sc.nextInt();
    System.out.println(" ");
    indice--;
    if (indice < 0 || indice >= lista.size()) {
      System.out.println("indice de tarea invalido");
    } else {
      lista.get(indice);
      if (tarea[3][0] == "Pendiente") {
        tarea[3][0] = "completado";
      } else {
        tarea[3][0] = "Pendiente";
      }
      System.out.println("Cambio hecho con exito");
    }
  }

  void borrarTarea() {
    System.out.print("Ingrese el indice de la ");
    System.out.println("tarea que desea eliminar");
    System.out.println(" ");
    System.out.println(" ");
    int indice = sc.nextInt();
    System.out.println(" ");
    indice--;
    if (indice < 0 || indice >= lista.size()) {
      System.out.println("indice de tarea invalido");
    } else {
      lista.remove(indice);
      System.out.println("Tarea eliminada con exito");
    }
  }
}