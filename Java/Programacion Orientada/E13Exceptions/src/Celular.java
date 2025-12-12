class Celular {
  short nivelBateria;
  boolean encendido;

  Celular() {
    nivelBateria = 100;
    encendido = false;
  }

  void encender() throws Exception {
      if (this.nivelBateria > 0) {
        System.out.println("Encendiendo dispositivo");
        encendido = true;
      } else {
        throw new Exception("Sin bateria");
      }
  }

  void llamar(String numero) throws Exception {
      if (this.encendido) {
        System.out.println("Llamando a " + numero);
      } else {
        throw new Exception("Apagado");
      }
  }
}