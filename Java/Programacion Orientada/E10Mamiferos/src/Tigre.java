import java.util.Random;
class Tigre extends Mamiferos {
  float tamaño;
  float peso;

  Tigre(float tamaño, float peso){
    super(4, true);
    this.tamaño = tamaño;
    this.peso = peso;
  }
  void Cazar() {
    String[] animales = {"mata un venado", "se come un niño", "se le quita el hambre"};
    Random random = new Random();
    int dialogos = random.nextInt(3);
    System.out.println("El tigre" + animales[dialogos]);
  }
}
