import javax.swing.*;
class PracticaJframe extends JFrame {
    PracticaJframe() {
      setLayout(null);
    }
    public static void main(String[] args) {
      PracticaJframe interfaz = new PracticaJframe();
      interfaz.setBounds(500, 200, 500, 500);
      interfaz.setVisible(true);
      //esto ignora lo que pongas sobre la posicion inicial
      //para ponerlo al centro
      interfaz.setLocationRelativeTo(null);
      //esto evita que el usuario cambie el tamaño de la interfaz
      interfaz.setResizable(false);
    }
}
