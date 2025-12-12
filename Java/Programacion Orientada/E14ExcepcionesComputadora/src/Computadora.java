class Computadora {
  Pantalla pantalla;
  boolean encendido;

  Computadora() {
    this.pantalla = new Pantalla();
  }

  void encender() throws Exception {
    this.encendido = true;
    encenderPantalla();
  }

  void encenderPantalla() throws Exception {
    if (encendido) {
      pantalla.encender();
    
    } else {
      throw new Exception("Computadora no encendida");
    }  
  }
}
