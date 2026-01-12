class App {
  public static void main(String[] args) throws Exception {
    Matriz matriz = new Matriz();
    int[][] a = {{1,2},{3,4}};
    matriz.MostrarMatriz(a);
    int[][] b = matriz.Traspuesta(a);
    matriz.MostrarMatriz(b);
  }
}