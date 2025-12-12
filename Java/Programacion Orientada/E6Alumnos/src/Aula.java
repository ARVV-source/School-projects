class Aula {
  String nombre;
  Asiento[] asientos;

  Aula(String nombre, int x) {
    this.nombre = nombre;
    this.asientos = new Asiento[x];
    for (int i = 0; i < asientos.length; i++) {
      asientos[i] = new Asiento(true);
    }
  }

  void entrar(Alumno alumno) {
    for (int i = 0; i < asientos.length; i++) {
      if (asientos[i].ocupante == alumno) {
        asientos[i].ocupado = true;
      }
    }
    System.out.println("________________________________________");
  }

  void salir(Alumno alumno) {
    for (int i = 0; i < asientos.length; i++) {
      if (asientos[i].ocupante == alumno) {
        asientos[i].ocupado = false;
      }
    }
    System.out.println("________________________________________");
  }

  void mostrarOcupantes() {
    for (int i = 0; i < asientos.length; i++) {
      if (asientos[i].ocupado == true) {
        System.out.println(asientos[i].ocupante.nombre + " se encuentra en su asiento");
      } else {
        System.out.println("No hay nadie en el asiento " + (i + 1));
      }
    }
    System.out.println("________________________________________2");
  }
}