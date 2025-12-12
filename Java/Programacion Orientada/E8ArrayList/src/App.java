import java.util.ArrayList;

class App {
  public static void main(String[] args) {
    ArrayList<String> nombres = new ArrayList<String>();
    String apellidoMaterno = "Gonzalez";
    String apellidoPaterno = "Arvizu";
    String nombre1 = "Christopher";
    String nombre2 = "Emilio";

    nombres.add(0, apellidoMaterno);
    nombres.add(0, apellidoPaterno);
    nombres.add(0, nombre2);
    nombres.add(0, nombre1);
    System.out.println(nombres);

    boolean contiene = nombres.contains("Mitsiu");
    System.out.println(contiene);

    System.out.println(nombres.indexOf(nombre1));

    System.out.println(nombres.indexOf(nombre1.toUpperCase()));
    
    nombres.replaceAll(stringAmayus -> stringAmayus.toUpperCase());
    System.out.println(nombres); 
  }   
}

