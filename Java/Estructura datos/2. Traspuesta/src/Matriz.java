class Matriz {
  int[][] Traspuesta(int[][] matriz) {
    int[][] matrizTras = new int[matriz[0].length][matriz.length];
    
    for(int f=0; f<matriz.length; f++){
      for(int c=0; c<matriz[0].length; c++) {
        matrizTras[c][f] = matriz[f][c];
      }
    }
    return matrizTras;
  }

  void MostrarMatriz(int[][] matriz) {
    for(int i=0; i<matriz.length; i++) {
      for (int j=0; j<matriz[0].length; j++) {
        System.out.print(matriz[j][i] + "  ");
      }
      System.out.println("");
    }
    System.out.println("");
    System.out.println("");
  }
}
