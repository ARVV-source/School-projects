class App {
  public static void main(String[] args) {
    Alumno a1 = new Alumno("Emilio Arvizu", "up240589");
    Alumno a2 = new Alumno("Juan Perez", "UP111111");
    Aula salon = new Aula("JuanGabriel", 3);
    salon.asientos[0].ocupante = a1;
    salon.asientos[1].ocupante = a2;
    salon.mostrarOcupantes();
    salon.entrar(a1);
    salon.mostrarOcupantes();
    salon.entrar(a2);
    salon.mostrarOcupantes();
    salon.salir(a1);
    salon.mostrarOcupantes();
  }
}
