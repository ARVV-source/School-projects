class Lapiz {
  int tamaño;
  String color;
  String marca;
  int cantidadGrafito;
  Grafito grafito;

  Lapiz(int size) {
    this.tamaño = size;
    this.cantidadGrafito = 50;
    grafito = new Grafito("media", "carbon");
  }

  void sacarPunta() throws Exception {
    if (tamaño < 1) {
      throw new IllegalStateException("No hay mas lapiz al que sacarle punta");
    }
    System.out.println("Sacando punta");
    tamaño --;
  }
}
