public class App {
    public static void main(String[] args) throws Exception {
      double PromPersona;
      double PromMateria;
      String[] nombres = { "Ana", "Luis", "Carlos", "Marta" };
      String[] materias = { "Matemáticas", "Física", "Química", "Biología" };
      double[][] calificaciones = {
              { 10, 9, 8, 7 },
              { 9, 7, 6, 8 },
              { 8, 9, 5, 9 },
              { 7, 8, 9, 10 }
      };
      for(int i=0; i<4; i++) {
        System.out.print("        " + materias[i]);
      }
      System.err.print("        promedio");
      System.err.println();
      for(int i=0; i<4; i++) {
        System.out.print(nombres[i]);
        PromPersona=0;
        for(int o=0; o<4; o++) {
          System.err.print("           " + calificaciones[i][o]);  
          PromPersona = calificaciones[i][o] + PromPersona;
        }
        PromPersona = PromPersona/4;
        System.err.println("             " + PromPersona);
      }
      System.out.print("promedio");
      for (int c=0; c<4; c++) {
        PromMateria=0;
        for (int f=0; f<4; f++){
          PromMateria = PromMateria + calificaciones[f][c];
        }
        PromMateria=PromMateria/4;
        System.out.print("         " + PromMateria);
      }
    }
  }

