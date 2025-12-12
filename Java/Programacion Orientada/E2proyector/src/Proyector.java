class Proyector {
  // Declaro atributos
  String tipoLente;
  String modelo;
  boolean encendido;

  // Declaro metodos
  Proyector(String tipoLente, String modelo) {
    this.tipoLente = tipoLente;
    this.modelo = modelo;
    this.encendido = false;
  }

  boolean presionarPowerButton() {
    if (encendido == false) {
      System.out.println("Encendiendo proyector...");
      encendido = true;
      return encendido;
    } else {
      System.out.println("Apagando proyector...");
      encendido = false;
      return encendido;
    }
  }

  void proyectar(String input) {
    if (encendido == true) {
      if (input == "HDMI") {
        System.out.println("Señal HDMI encontrada");
      } else {
        System.out.println("Señal no encontrada");
      }
    } else {
      return;
    }
  }
}
