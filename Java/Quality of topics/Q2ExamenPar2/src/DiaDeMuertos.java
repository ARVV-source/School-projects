import java.util.ArrayList;

class DiaDeMuertos extends DiaFestivo {
  boolean ponerAltar(ArrayList<String> ofrendas, int numOfrendas) {
    try {
      ofrendas.get(0); //nacada para forzar el out of Bounds
      for (int index = 0; index < numOfrendas; index++) {
        System.out.println(ofrendas.get(index));
      }
      return true;
    } catch (IndexOutOfBoundsException ex) {
      System.out.println("Este altar no es digno");
      return false;
    }
  }

  boolean celebrar(String eslogan, ArrayList<String> ofrendas) {
    boolean completado = this.ponerAltar(ofrendas, ofrendas.size());  
    
    if (!completado) {
      System.out.println("Todo se cancela");
      return false;
    }
    System.out.println(eslogan);
    return super.celebrar();
  }
}

