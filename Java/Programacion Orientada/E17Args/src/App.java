public class App {
  public static void main(String[] args) {
    for(String a : args) {
      System.out.println(a);
    }

    if("dev".equals(args[0])) {
      System.out.println("contexto de desarrollo");
    }
  }
}

