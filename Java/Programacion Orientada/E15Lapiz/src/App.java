class App {
    public static void main(String[] args) throws Exception {
      Lapiz lapis = new Lapiz(10);
      try{
        for (int i=0; i<11; i++ ){
          lapis.sacarPunta();
        }
      } catch (IllegalStateException ex) {
        System.out.println(ex);
      }
    }
}
