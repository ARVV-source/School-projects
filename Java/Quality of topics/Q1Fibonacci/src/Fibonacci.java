class Fibonacci {
  public static void main(String[] args) {
    //1 < var < 46
    Fibonacci f = new Fibonacci();
    int[] serie = f.generateFibSerie(46);
    printSerie(serie);
  }
  
  int[] generateFibSerie(int cant) {
    try {
      int[] newSerie = new int[cant];
      System.out.println("ok");
      newSerie[0] = 1;
      newSerie[1] = 1;

      for (int i = 2; i < cant; i++) {
        newSerie[i] = newSerie[i - 1] + newSerie[i - 2];
      }
      return newSerie;
    } catch (NegativeArraySizeException e) {
      System.out.println("No se pueden utilizar variables negativas");
      return new int[0];
    } catch (ArrayIndexOutOfBoundsException e) {
      System.out.println("No se pueden utilizar variables menores a 2");
      return new int[0];
    }
    
  }
  

  static void printSerie(int[] pserie) {
    for (int num : pserie) {
      System.out.println(num);
    }
  }
}