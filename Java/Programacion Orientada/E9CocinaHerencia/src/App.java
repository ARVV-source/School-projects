class App {

  public static void main(String[] args) throws Exception {
    Cocina cocina = new Cocina();
    cocina.muebles.add("Estufa");
    Persona persona1 = new Persona("Juan");
    
    cocina.observar(persona1, cocina.muebles);
    cocina.entrar(persona1);
    cocina.observar(persona1, cocina.muebles);
    cocina.salir(persona1);
  }
}
