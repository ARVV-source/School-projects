public class Main {
  public static void main(String[] args) {
    Celular celular = new Celular();
    try {
    celular.llamar("449 386 0585");
    celular.encender();
    celular.llamar("449 386 0585");
    } catch (Exception ex) {
      System.out.println(ex);
    }

    try {
    celular.encender();
    celular.llamar("449 386 0585");
    } catch (Exception ex) {
      System.out.println(ex);
    }
  }
}