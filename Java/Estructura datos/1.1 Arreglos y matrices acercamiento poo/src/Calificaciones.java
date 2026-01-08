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
    promPersona=promPersona/calificaciones[persona].length;
    return promPersona;
  }

  public double PromMateria(int materia) {
    double promMateria=0;
    for(int a=0; a<calificaciones[materia].length; a++) {
      promMateria = promMateria + calificaciones[a][materia];
    }
    promMateria=promMateria/calificaciones[materia].length;
    return promMateria;
  }

  public void ImprimirTabla() {
    System.out.print("     ");
    for(int i=0; i<materias.length; i++) {
      System.out.print("      " + materias[i]);
    }
    System.out.print("    promedio");
    for(int p=0; p<materias.length; p++) {
      System.out.println();
      /*con String Format se da formato el 8 representa el
       ancho que requiere la parte que es el espacio de los nombres*/
      System.out.print(String.format("%8s", nombres[p]));
      for(int c=0; c<materias.length; c++) {
        System.out.print("         " + calificaciones[p][c]);
      }
      System.out.print("          " + PromPersona(p));
    }
    System.out.println();
    System.out.print("promedio");
    for(int m=0; m<calificaciones.length; m++) {
      System.out.print("         " + PromMateria(m));
    }
  }
}
