import javax.swing.*;
class PracticaJframe extends JFrame {
  //intentar hacer los label privados por si se tiene mas de una ui
  private JLabel label1;
  private JLabel label2;
  PracticaJframe() {
    //setLayout indica que usas coords
      setLayout(null);
      label1 = new JLabel("Calculadora");
      label1.setBounds(10, 10, 300, 30);
      //add es para agregar un elemento al Jframe
      add(label1);
      label2 = new JLabel("Ingrese un numero aronou igual ni funciona");
      label2.setBounds(10, 40, 300, 30);
      add(label2);
    }
    public static void main(String[] args) {
      PracticaJframe interfaz = new PracticaJframe();
      interfaz.setBounds(0, 0, 500, 500);
      interfaz.setVisible(true);
      //esto ignora lo que pongas sobre la posicion inicial
      //para ponerlo al centro
      interfaz.setLocationRelativeTo(null);
      //esto evita que el usuario cambie el tamaño de la interfaz
      interfaz.setResizable(false);
    }
}
