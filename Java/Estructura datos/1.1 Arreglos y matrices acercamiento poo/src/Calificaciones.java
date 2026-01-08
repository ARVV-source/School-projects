class Calificaciones {
  public String[] nombres = { "Ana", "Luis", "Carlos", "Marta" };
  public String[] materias = { "Matemáticas", "Física", "Química", "Biología" };
  public double[][] calificaciones = {
    { 10, 9, 8, 7 },
    { 9, 7, 6, 8 },
    { 8, 9, 5, 9 },
    { 7, 8, 9, 10 }
    };

  public double PromPersona(int persona) {
    double promPersona=0;
    for(int a=0; a<calificaciones[persona].length; a++) {
      promPersona = promPersona + calificaciones[persona][a];
    }
    promPersona=promPersona/4;
    return promPersona;
  }

  public void ImprimirTabla() {
    for(int i=0; i<materias.length; i++) {
      System.out.print("         " + materias[i]);
    }
    
  }
}
