class Dron {
  float lat;
  float alt;
  float lon;
  static boolean regresarABase;

  Dron (float lat, float alt, float lon) {
    this.lat = lat;
    this.alt = alt;
    this.lon = lon;
  }

  static void printRegresarABase() {
  System.out.println(Dron.regresarABase);
  }
}