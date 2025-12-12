import java.util.ArrayList;

class Electronico {
  boolean encendido;
  String modelo;
  String marca;
  int anio;
  ArrayList<Componente> componentes;

  Electronico(boolean encendido, String modelo, String marca, int anio) {
    this.encendido = encendido;
    this.modelo = modelo;
    this.marca = marca;
    this.anio = anio;
  }
  
  boolean encender() {
    encendido = true;
    System.out.println("Encendiendo dispositivo");
    return encendido;
    
  }

  boolean apagar() {
    encendido = false;
    System.out.println("Apagando dispositivo");
    return encendido;
    
  }
  
}
