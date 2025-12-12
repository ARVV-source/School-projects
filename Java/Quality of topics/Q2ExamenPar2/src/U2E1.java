import java.util.ArrayList;

class U2E1 {
  public static void main(String[] args) {
    ArrayList<String> x = new ArrayList<String>();
    x.add("Flores");
    x.add("Velas");
    x.add("Tequila");
    DiaDeMuertos mejorCelebracion = new DiaDeMuertos();
    mejorCelebracion.celebrar("Me da mi calaverita", x);
  }
}
