class App {
  public static void main(String[] args) throws Exception {
    Proyector proyector = new Proyector("Abierto", "AK748");
    proyector.presionarPowerButton();
    proyector.proyectar("HDMI");
    proyector.presionarPowerButton();
    proyector.proyectar("HDMI");
  }
}
