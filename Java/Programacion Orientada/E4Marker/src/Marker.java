class Marker {
  short nivelDeTinta;
  String colorTinta;
  String codigoColor;

  Marker(String colorTinta) {
    this.nivelDeTinta = 100;
    this.colorTinta = colorTinta;

    switch (this.colorTinta) {
      case "Rojo":
        this.codigoColor = "\u001B[31m";
        break;
      case "Verde":
        this.codigoColor = "\u001B[32m";
        break;
      case "Azul":
        this.codigoColor = "\u001B[34m";
        break;
      default:
        this.codigoColor = "\u001B[0m";
        break;
    }
  }

  void Escribir(String texto) {
    System.out.println(this.codigoColor);
    for (char palabras : texto.toCharArray()) {
      if (palabras == ' ') {
        System.out.print(palabras);
      } else {
        System.out.print(palabras);
        nivelDeTinta--;
      }
    }
    System.out.println("\u001B[0m");
    System.out.println("\nEl nivel de tinta es: " + nivelDeTinta);
  }
}
