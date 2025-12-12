import javax.swing.*;
//Jframe permite hacer contenedores para elementos graficos
class Formulario extends JFrame {
  //etiqueta (para mostrar datos en pantalla)
  //se hace privado para solo usarlo aqui
  private JLabel label1 = new JLabel("Hola, Mundo!");

  Formulario() {
  //indica por ordenadas donde ira un elemento
  setLayout(null);
  label1.setBounds(10,20, 200, 300);
  add(label1);
  }
  public static void main(String[] args) {
    Formulario formulario = new Formulario();
    formulario.setBounds(0,0,300,400);
    formulario.setVisible(true);
    //sirve para decir que quieres que aparezca al centro de la pantalla
    formulario.setLocationRelativeTo(null);
  } 
}