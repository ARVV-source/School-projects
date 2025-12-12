class Contador {
  private int numero;

  Contador() {
    this.numero = 0;
  }
  void aumentarNum(){
    this.numero++;
  }
  public void verNumero() {
    System.out.println(this.numero);
  }
}