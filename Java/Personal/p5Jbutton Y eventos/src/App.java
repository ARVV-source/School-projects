import javax.swing.*;
//libreria para eventos en uis
import java.awt.event.*;
//actionListener hace que el usuario pueda interactuar con la interfaz
class Interfaz extends JFrame implements ActionListener {
  JButton boton1;
  Interfaz() {
    setLayout(null);
    boton1 = new JButton("cierra");
    boton1.setBounds(200,100,80,40);
    add(boton1);
    //le agregas un evento al botton, this dice que es dentro del boton
    boton1.addActionListener(this);
  }

  //la e sirve para crear una variable en la que se guarde el evento
  public void func(ActionEvent e) {
    //getSource dice donde ocurrio el evento osea de que boton vino
    if (e.getSource() == boton1) {
      //cierra la interfaz
      System.exit(0);
    }
  }

  public static void main(String[] args) {
    Interfaz interfaz = new Interfaz();
    interfaz.setBounds(0,0,500,500);
    interfaz.setVisible(true);
    interfaz.setLocationRelativeTo(null);
  }
}
