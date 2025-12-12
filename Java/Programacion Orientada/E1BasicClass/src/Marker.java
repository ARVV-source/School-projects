class Marker {
  short nivelDeTinta;
  String nombreColor;
  
  Marker(String nombreColor) {
    this.nombreColor = nombreColor;
    this.nivelDeTinta = 100;
  }

  void escribir(String palabras) {
    // System.out.println(palabras);
    for (char letra : palabras.toCharArray()) {
      if (this.nivelDeTinta == 0) {
        break;
      } else {
        if (letra == ' ') {
          System.out.print(letra);
        } else {
          System.out.print(letra);
          this.nivelDeTinta = (short) (this.nivelDeTinta--);
        }
      }
    }
  }
}
