public class App {
    public static void main(String[] args) throws Exception {
      Dron d1 = new Dron(10, 10, 10);
      Dron d2 = new Dron(5, 5, 10);
      Dron d3 = new Dron(-10, -10, 10);
      Dron array[] = new Dron[3];
        array[0] = d1;
        array[1] = d2;
        array[2] = d3;

      for(Dron a : array){
        System.out.println(a.lat);
        System.out.println(a.regresarABase);
      }
      d3.regresarABase = true;

      for(Dron a : array){
        System.out.println(a.regresarABase);
    }
    System.out.println("----------------");
    System.out.println(Dron.regresarABase);

    Dron.regresarABase = true;
    Dron.printRegresarABase();
    System.out.println(Dron.regresarABase);
  }
}
