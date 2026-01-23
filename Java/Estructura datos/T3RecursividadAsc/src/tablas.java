public class tablas {
  void TablaAsc(int tabla, int cant, int contador) {
    if (contador < cant) {
      System.out.println(tabla + "x" + contador + "=" + (tabla * contador));
      TablaAsc(tabla, cant, contador + 1);
    } else {
      System.out.println(tabla + "x" + contador + "=" + (tabla * contador));
    }
    }

  void TablaDesc(int tabla, int cant) {
    if (1 < cant) {
      System.out.println(tabla + "x" + cant + "=" + (tabla * cant));
      TablaDesc(tabla, cant - 1);
    } else {
      System.out.println(tabla + "x" + cant + "=" + (tabla * cant));
    }
  }
}
class prueba {
  public static void main(String[] args) {
    tablas x = new tablas();
    x.TablaAsc(5, 10, 1);
    System.out.println("");
    x.TablaDesc(5, 10);
  }
}