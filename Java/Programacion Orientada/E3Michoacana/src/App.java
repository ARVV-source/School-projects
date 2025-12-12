class E3Michoacana2 {
  public static void main(String[] args) {
    // Se instancia un objeto paleteria de la clase Michoacana//
    Michoacana paleteria = new Michoacana("Av. Lazaro Cardenas 453");
    // Se instancian personas a la clase Personas//
    Persona persona1 = new Persona("Jorge", "Gerente", (short) 27);
    Persona persona2 = new Persona("Estefany", "Cajero", (short) 18);
    Persona persona3 = new Persona("Pepe", "Cajero", (short) 22);
    // Se meten las personas al Arraylist Empleado el cual es un atributo de la
    // paleteria//
    paleteria.Empleado.add(persona1);
    paleteria.Empleado.add(persona2);
    paleteria.Empleado.add(persona3);
    // Se hace un print del retun de paletera.Empleado (el ArrayList)//
    System.out.println("Empleados: " + paleteria.Empleado);

    // Se instancian objetos a la clase Helado//
    Helado helado1 = new Helado("Fresa", (short) 10);
    Helado helado2 = new Helado("Chocolate", (short) 12);

    // se meten los objetos a el ArrayList helado de paleteria//
    paleteria.helado.add(helado1);
    paleteria.helado.add(helado2);

    // Se hace un print del retun de paletera.helado (el ArrayList)//
    for (int i = 0; i < paleteria.helado.size(); i++) {
      System.out.println("Helados: " + paleteria.helado.get(i));
    }
  }
}