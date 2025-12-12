class App {
  public static void main(String[] args) {
    String matriz [][] = new String[4][3];  
    matriz [0][0] = "Emilio"; matriz [0][1] = "Gonzalez"; matriz [0][2] = "Ruiz";
    matriz [1][0] = "Angel"; matriz [1][1] = "Paredes"; matriz [1][2] = "Muro";
    matriz [2][0] = "Daniela"; matriz [2][1] = "Martinez"; matriz [2][2] = "Garza";
    matriz [3][0] = "Juan"; matriz [3][1] = "Perez"; matriz [3][2] = "soto";

    for (int i = 0; i < 4; i++) {
      for (int j = 0; j < 3; j++) {
        System.out.print(matriz[i][j] + " ");
      }
      System.out.println(" ");
    }
    
  }
}
