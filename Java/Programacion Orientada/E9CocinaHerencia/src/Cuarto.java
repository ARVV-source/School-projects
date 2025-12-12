import java.util.ArrayList;

class Cuarto {
  float altura;
  float ancho;
  float largo;
  ArrayList<Persona> interior;

  Cuarto() {
    this.altura = 1;
    this.ancho = 1;
    this.largo = 1;
    this.interior = new ArrayList<Persona>();
  }

  void entrar(Persona persona) {
    interior.add(persona);
    boolean result = interior.add(persona);
    if (result) {
      System.out.println(persona.nombre + " a entrado");
    } else {
      System.out.println(persona.nombre + " no fue capaz de entrar");
    }
  }

  void salir(Persona persona) {
    interior.remove(persona);
    boolean result = interior.remove(persona);
    if (result) {
      System.out.println(persona.nombre + " a salido");
    } else {
      System.out.println(persona.nombre + " no fue capaz de salir");
    }
  }

  void observar(Persona persona, ArrayList<String> objetos) {
    if (interior.contains(persona)) {
      System.out.println(objetos);
    } else {
      System.out.println(persona.nombre + " no esta dentro de un cuarto");
    }
  }
}