class App {
  public static void main(String[] args) {
    Computadora computadora = new Computadora();
    try {
      computadora.encenderPantalla();
    } catch (Exception ex) {
      System.out.println(ex);
    }
  }
}
