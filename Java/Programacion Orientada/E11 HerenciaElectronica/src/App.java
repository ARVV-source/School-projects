public class App {
  public static void main(String[] args) throws Exception {
    Componente pantalla = new Componente("Bateria", 100, "Dar energia al dispositivo");
    Celular aifon = new Celular(false, "iphone 1", "apol", 2001);
    aifon.componentes.add(pantalla);
    aifon.encender();
    aifon.llamada("Juan");
    aifon.apagar();
    aifon.llamada("Juan");
  }
}
