import java.util.ArrayList;
import java.util.Random;

class Celular extends Electronico {
  int almacenamiento;
  ArrayList<App> aplicacion;
  int nivelCarga;

  Celular(boolean encendido, String modelo, String marca, int anio) {
    super(encendido, modelo, marca, anio);
    this.componentes = new ArrayList<Componente>();
  }
  
  int llamada (String dest) {
    if (encendido) {
    Random random = new Random();
    int duracion = random.nextInt(100);
    System.out.println("La llamada con " + dest + " duro " + duracion + " minutos");
    return duracion;
    } else {
      return 0;
    }
  }
}
